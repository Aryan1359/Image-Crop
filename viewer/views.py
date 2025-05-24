import os
from django.shortcuts import render, redirect
from django.conf import settings

from extractor.ocr import extract_and_append_text


image_list = []
current_index = 0

def home(request):
    global image_list, current_index

    if request.method == 'POST':
        folder_path = request.POST.get('folder_path')
        if os.path.isdir(folder_path):
            request.session['folder_path'] = folder_path
            image_list.clear()
            for file in sorted(os.listdir(folder_path)):
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    image_list.append(file)
            current_index = 0
        return redirect('viewer_home')

    folder_path = request.session.get('folder_path', '')
    image_path = None
    if folder_path and image_list:
        image_name = image_list[current_index]
        source_path = os.path.join(folder_path, image_name)
        dest_folder = os.path.join(settings.MEDIA_ROOT, 'media_temp')
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, image_name)
        with open(source_path, 'rb') as fsrc, open(dest_path, 'wb') as fdst:
            fdst.write(fsrc.read())
        image_path = f"media_temp/{image_name}"

    return render(request, 'viewer/home.html', {
        'image_path': image_path,
        'has_prev': current_index > 0,
        'has_next': current_index < len(image_list) - 1,
    })

def next_image(request):
    global current_index
    if current_index < len(image_list) - 1:
        current_index += 1
    return redirect('viewer_home')

def prev_image(request):
    global current_index
    if current_index > 0:
        current_index -= 1
    return redirect('viewer_home')


def delete_image(request):
    global current_index, image_list

    folder_path = request.session.get('folder_path', '')
    if not folder_path or not image_list:
        return redirect('viewer_home')

    image_name = image_list[current_index]
    image_path = os.path.join(folder_path, image_name)

    if os.path.exists(image_path):
        os.remove(image_path)

    # Remove from list
    image_list.pop(current_index)

    # Adjust index
    if current_index >= len(image_list):
        current_index = max(0, len(image_list) - 1)

    return redirect('viewer_home')


import json
from PIL import Image
from django.http import JsonResponse

def crop_image(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        crop = body['cropData']
        label = body['label']

        folder_path = request.session.get('folder_path', '')
        if not folder_path or not image_list:
            return JsonResponse({'error': 'Missing data'}, status=400)

        image_name = image_list[current_index]
        image_path = os.path.join(folder_path, image_name)

        try:
            img = Image.open(image_path)
            x, y, w, h = map(int, [crop['x'], crop['y'], crop['width'], crop['height']])
            cropped = img.crop((x, y, x + w, y + h))

            ext = os.path.splitext(image_name)[1]
            new_name = f"{label}_{image_name}"
            save_path = os.path.join(folder_path, new_name)

            cropped.save(save_path)

            extract_and_append_text(save_path, label)





            # Delete original image
            if os.path.exists(image_path):
                os.remove(image_path)

            # Update in-memory list
            image_list[current_index] = new_name

            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
