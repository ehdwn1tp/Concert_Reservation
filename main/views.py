from django.shortcuts import render
import os

STATIC_DIR = 'C:/Users/LukeLim/OneDrive/바탕 화면/Projects/SideProject/Yolo_reservation/yolo_reservation/yolo_reservation/static'

# Create your views here.
def home(req):
    return render(req, 'home.html', {})


def performance(req):
    # DB 연결 후 이미지 파일 및 공연 정보 교체 필요
    img_src = sorted(os.listdir(os.path.join(STATIC_DIR, 'images')))
    generation = [
        ['33기', 'Dear Dreamers', '23년 8월 26-27일', 'NH아트홀'],
        ['11기', '지킬 앤 하이드', '22년 3월 26-27일', '광화문아트홀'],
        ['10기', '맘마미아', '22년 2월 19-20일', '인사아트홀'],
        ['42기', '무인도 탈출기', '23년 12월 29-31일', '안똔체홉극장'],
        ['40기', 'Re,', '24년 1월 20-21일', 'NH아트홀'],
        ['38기', 'TURN', '24년 1월 11-12일', '대학로 선돌극장'],
        ['16기', '빨래', '23년 8월 11-21일', '예술나무씨어터']
    ]

    # generation = list(zip(*generation))
    # information = [tuple(img_src)] + generation 

    information = list(zip(img_src, generation))

    print(information)
    return render(
        req,
        'performances.html', 
        {
            'img':information[0],
            'gen':information[1],
            'name':information[2],
            'date':information[3],
            'theater':information[4]
        }
    )


def reservation(req):
    return render(req, 'reservation.html', {})
    

def confirmation(req):
    return render(req, 'confirmation.html', {})


def change(req):
    return render(req, 'change.html', {})


def cancel(req):
    return render(req, 'cancel.html', {})

if __name__ == '__main__':
    performance('1')