from django.db import models
from django.utils import timezone

# Create your models here.
class Theater(models.Model):
    theater_id = models.AutoField('극장ID', primary_key=True)
    theater_name = models.CharField('극장명', max_length=20)
    theater_address = models.CharField('극장 주소', max_length=50)
    theater_price = models.IntegerField('대관료')
    theater_contact = models.CharField(max_length=20, verbose_name='극장 연락처')
    theater_size = models.SmallIntegerField('수용가능인원')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 일자')


class Play(models.Model):
    idx = models.AutoField(primary_key=True)
    play_id = models.CharField(max_length=5, unique=True, verbose_name='작품ID') # 작품 종류(play_type) 1자리(연극 1, 뮤지컬 2) + 작품 번호(idx) 4자리 ex) 10001
    play_type = models.BooleanField('작품 종류') # True: 뮤지컬, False: 연극
    play_name = models.CharField(unique=True, max_length=20, verbose_name='작품명')
    play_license = models.BooleanField() # True: 있음, False: 없음
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 일자')


class Performance(models.Model): # 포스터/작품 설명/기수
    idx = models.AutoField(primary_key=True)
    prf_id = models.CharField(max_length=10, verbose_name='공연 번호') # 작품ID(6자리 ) + 공연 날짜 + 시간 ()
    prf_play_id = models.ForeignKey(Play, on_delete=models.CASCADE)
    prf_changed_name = models.CharField(max_length=20, verbose_name='공연 변경 제목')
    prf_number = models.SmallIntegerField('공연 회차')
    prf_time = models.CharField(max_length=10, verbose_name='공연 시간')
    prf_theater_id = models.ForeignKey(Theater, on_delete=models.CASCADE) # 극장 ID
    # prf_generation = models.SmallIntegerField('기수')
    prf_actors = models.TextField(null=True, verbose_name='관계자 명단')
    # prf_poster = models.ImageField('포스터', null=True, blank=True)
    # prf_description = models.TextField('작품 설명', null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 일자')


class Reservation(models.Model):
    idx = models.AutoField(primary_key=True)
    reservation_id = models.IntegerField(verbose_name='예약 번호')
    reservation_phone = models.CharField(max_length=11, verbose_name='예매자 연락처')
    reservation_name = models.CharField(max_length=10, verbose_name='예매자 이름')
    reservation_cnt = models.SmallIntegerField(verbose_name='예매 인원')
    reservation_prf_id = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation_actors = models.TextField(verbose_name='지인 명단')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 일자')