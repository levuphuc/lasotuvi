# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from lasotuvi.AmDuong import (canChiNgay, canChiNam, diaChi, ngayThangNam, ngayThangNamCanChi, nguHanh, nguHanhNapAm, 
    thienCan, timCuc, sinhKhac, tinh_can_luong_bat_tu, format_can_luong, binh_giai_can_luong, xac_dinh_am_duong_thuan_nghich_ly)
from lasotuvi.Lich_HND import jdFromDate

from datetime import datetime
import time

class lapThienBan(object):
    def __init__(self, nn, tt, nnnn, gioSinh, gioiTinh, ten, diaBan,
                 duongLich=True, timeZone=7):
        super(lapThienBan, self).__init__()
        self.gioiTinh = 1 if gioiTinh == 1 else -1
        self.namNu = "Nam" if gioiTinh == 1 else "Nữ"

        self.canChiNamXemLaSo = canChiNam(datetime.now().year)


        chiGioSinh = diaChi[gioSinh]
        canGioSinh = ((jdFromDate(nn, tt, nnnn) - 1) * 2 % 10 + gioSinh) % 10
        if canGioSinh == 0:
            canGioSinh = 10
        self.chiGioSinh = chiGioSinh
        self.canGioSinh = canGioSinh
        self.gioSinh = "{} {}".format(thienCan[canGioSinh]['tenCan'],
                                      chiGioSinh['tenChi'])

        self.timeZone = timeZone
        self.today = time.strftime("%d/%m/%Y")
        self.ngayDuong, self.thangDuong, self.namDuong, self.ten = \
            nn, tt, nnnn, ten
        if duongLich is True:
            self.ngayAm, self.thangAm, self.namAm, self.thangNhuan = \
                ngayThangNam(self.ngayDuong, self.thangDuong, self.namDuong,
                             True, self.timeZone)
        else:
            self.ngayAm, self.thangAm, self.namAm = self.ngayDuong,\
                self.thangDuong, self.namDuong

        self.canThang, self.canNam, self.chiNam = \
            ngayThangNamCanChi(self.ngayAm, self.thangAm,
                               self.namAm, False, self.timeZone)
        self.chiThang = self.thangAm
        self.canThangTen = thienCan[self.canThang]['tenCan']
        self.canNamTen = thienCan[self.canNam]['tenCan']
        # Vì tháng Giêng = Dần = chi số 2 => offset +2 so với index tháng, và hiện tại có Chi Hẻm Có nên phải chia 13
        self.chiThangTen = diaChi[(self.thangAm + 2) % 13]['tenChi']

        self.chiNamTen = diaChi[self.chiNam]['tenChi']

        self.canNgay, self.chiNgay = canChiNgay(
            self.ngayDuong, self.thangDuong, self.namDuong,
            duongLich, timeZone)
        self.canNgayTen = thienCan[self.canNgay]['tenCan']
        self.chiNgayTen = diaChi[self.chiNgay]['tenChi']

        cungAmDuong = 1 if (diaBan.cungMenh % 2 == 1) else -1
        self.amDuongNamSinh = "Dương" if (self.chiNam % 2 == 1) else "Âm"


        self.amDuongMenh = xac_dinh_am_duong_thuan_nghich_ly(self.canNamTen,self.thangAm, self.ngayAm,chiGioSinh['tenChi'])

        # if (cungAmDuong * self.gioiTinh == 1):
        #     self.amDuongMenh = "Âm dương thuận lý"
        # else:
        #     self.amDuongMenh = "Âm dương nghịch lý"

        cuc = timCuc(diaBan.cungMenh, self.canNam)
        self.hanhCuc = nguHanh(cuc)['id']
        self.tenCuc = nguHanh(cuc)['tenCuc']
        # tinh_can_luong_bat_tu(canNamTen, chiNamTen, thangAm, ngayAm, chiGioTen):     
        intCanLuongSo = tinh_can_luong_bat_tu(self.canNamTen, self.chiNamTen, self.thangAm, self.ngayAm, self.gioSinh.split()[-1])

        self.canLuong = format_can_luong(intCanLuongSo)
        self.canLuongBinhGiai = binh_giai_can_luong(intCanLuongSo)  # chuỗi giải nghĩa

        self.menhChu = diaChi[self.chiNam]['menhChu']
        self.thanChu = diaChi[self.chiNam]['thanChu']


        self.menh = nguHanhNapAm(self.chiNam, self.canNam)
        menhId = nguHanh(self.menh)['id']
        menhCuc = sinhKhac(menhId, self.hanhCuc)
        if menhCuc == 1:
            self.sinhKhac = "Bản Mệnh sinh Cục"
        elif menhCuc == -1:
            self.sinhKhac = "Bản Mệnh khắc Cục"
        elif menhCuc == -1j:
            self.sinhKhac = "Cục khắc Bản Mệnh"
        elif menhCuc == 1j:
            self.sinhKhac = "Cục sinh Bản mệnh"
        else:
            self.sinhKhac = "Cục hòa Bản Mệnh"

        self.banMenh = nguHanhNapAm(self.chiNam, self.canNam, True)
