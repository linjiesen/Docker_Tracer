from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_exempt

from web.forms.wiki import WikiModelForm
from web import models

from utils.encrypt import uid
from utils.tencent.cos import upload_file


def wiki(request, project_id):
    """wiki的首页展示"""
    wiki_id = request.GET.get('wiki_id')
    if not wiki_id or not wiki_id.isdecimal():
        return render(request, 'wiki.html')

    wiki_object = models.Wiki.objects.filter(id=wiki_id, project_id=project_id).first()

    return render(request, 'wiki.html', {'wiki_object': wiki_object})


def wiki_add(request, project_id):
    """wiki添加"""
    # wiki_object = models.Wiki.objects.filter(project_id=project_id).first()
    #
    # if not wiki_object:
    #     url = reverse('wiki', kwargs={'project_id': project_id})
    #     return redirect(url)
    if request.method == 'GET':
        form = WikiModelForm(request)
        return render(request, 'wiki_form.html', {'form': form})
        # return render(request, 'wiki_form.html', {'form': form, 'wiki_object': wiki_object})
    form = WikiModelForm(request, request.POST)
    if form.is_valid():
        if form.instance.parent:
            form.instance.depth = form.instance.parent.depth + 1
        else:
            form.instance.depth = 1

        form.instance.project = request.tracer.project
        form.save()
        url = reverse('wiki', kwargs={'project_id': project_id})
        return redirect(url)
    return render(request, 'wiki_form.html', {'form': form})


def wiki_catalog(request, project_id):
    """wiki目录"""

    # 获取当前项目所有的目录
    data = models.Wiki.objects.filter(project=request.tracer.project).values("id", 'title', 'parent_id').order_by(
        'depth',
        'id')

    return JsonResponse({'status': True, 'data': list(data)})


def wiki_delete(request, project_id, wiki_id):
    """删除文章"""

    models.Wiki.objects.filter(project_id=project_id, id=wiki_id).delete()

    url = reverse('wiki', kwargs={'project_id': project_id})
    return redirect(url)


def wiki_edit(request, project_id, wiki_id):
    """编辑文章"""

    wiki_object = models.Wiki.objects.filter(project_id=project_id, id=wiki_id).first()

    if not wiki_object:
        url = reverse('wiki', kwargs={'project_id': project_id})
        return redirect(url)
    if request.method == 'GET':
        form = WikiModelForm(request, instance=wiki_object)
        return render(request, 'wiki_form.html', {'form': form, 'wiki_object': wiki_object})

    form = WikiModelForm(request, data=request.POST, instance=wiki_object)
    if form.is_valid():
        if form.instance.parent:
            form.instance.depth = form.instance.parent.depth + 1
        else:
            form.instance.depth = 1

        form.instance.project = request.tracer.project
        form.save()
        url = reverse('wiki', kwargs={'project_id': project_id})
        preview_url = "{0}?wiki_id={1}".format(url, wiki_id)
        return redirect(preview_url)

    return render(request, 'wiki_form.html', {'form': form})


# 网页中无法添加csrf token， 可在view函数处添加装饰器csrf_exempt(存放于包django.views.decorators.csrf中)
@xframe_options_exempt
@csrf_exempt
def wiki_upload(request, project_id):
    """
    markdown插件上传图片
    """
    result = {
        'success': 0,
        'message': None,
        'url': None,
    }

    image_object = request.FILES.get('editormd-image-files')
    if not image_object:
        result['message'] = "文件不存在"
        return JsonResponse(result)

    ext = image_object.name.rsplit('.')[-1]  # 获取文件后缀名
    key = "{}.{}".format(uid(request.tracer.user.mobile_phone), ext)

    # 文件对象上传到当前项目的桶中
    image_url = upload_file(
        bucket=request.tracer.project.bucket,
        region=request.tracer.project.region,
        file_object=image_object,
        key=key,
    )
    print(image_url)

    result = {
        'success': 1,
        'message': None,
        'url': image_url,
    }
    print(result)
    print(JsonResponse(result))
    return JsonResponse(result)

