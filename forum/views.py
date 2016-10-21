#from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block

def index(request):
    block_infos = Block.objects.filter(status=0).order_by("id")
    #block_infos = [
    #    {"name":"运维专区", "desc":"运维人员看过来", "manager":"Terry", "link":"http://baidu.com"},
    #    {"name":"Python专区", "desc":"2.7还是3.5？", "manager":"Nicole", "link":"http://google.com"},
    #    {"name":"Django专区", "desc":"快速开发Web应用", "manager":"寿司", "link":"http://163.com"}
    #]
    return render(request, "index.html", {"blocks":block_infos})
