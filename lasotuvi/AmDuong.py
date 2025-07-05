# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""

from lasotuvi.Lich_HND import S2L, L2S, jdFromDate


thienCan = [
    {
        "id": 0,
        "chuCaiDau": None,
        "tenCan": None,
        "nguHanh": None,
        "nguHanhID": None,
        "vitriDiaBan": None,
        'amDuong': None
    },
    {
        "id": 1,
        "chuCaiDau": "G",
        "tenCan": "Giáp",
        "nguHanh": "M",
        "nguHanhID": 2,
        "vitriDiaBan": 3,
        'amDuong': 1
    },
    {
        "id": 2,
        "chuCaiDau": "A",
        "tenCan": "Ất",
        "nguHanh": "M",
        "nguHanhID": 2,
        "vitriDiaBan": 4,
        'amDuong': -1
    },
    {
        "id": 3,
        "chuCaiDau": "B",
        "tenCan": "Bính",
        "nguHanh": "H",
        "nguHanhID": 4,
        "vitriDiaBan": 6,
        'amDuong': 1
    },
    {
        "id": 4,
        "chuCaiDau": "D",
        "tenCan": "Đinh",
        "nguHanh": "H",
        "nguHanhID": 4,
        "vitriDiaBan": 7,
        'amDuong': -1
    },
    {
        "id": 5,
        "chuCaiDau": "M",
        "tenCan": "Mậu",
        "nguHanh": "O",
        "nguHanhID": 5,
        "vitriDiaBan": 6,
        'amDuong': 1
    },
    {
        "id": 6,
        "chuCaiDau": "K",
        "tenCan": "Kỷ",
        "nguHanh": "O",
        "nguHanhID": 5,
        "vitriDiaBan": 7,
        'amDuong': -1
    },
    {
        "id": 7,
        "chuCaiDau": "C",
        "tenCan": "Canh",
        "nguHanh": "K",
        "nguHanhID": 1,
        "vitriDiaBan": 9,
        'amDuong': 1
    },
    {
        "id": 8,
        "chuCaiDau": "T",
        "tenCan": "Tân",
        "nguHanh": "K",
        "nguHanhID": 1,
        "vitriDiaBan": 10,
        'amDuong': -1
    },
    {
        "id": 9,
        "chuCaiDau": "N",
        "tenCan": "Nhâm",
        "nguHanh": "T",
        "nguHanhID": 3,
        "vitriDiaBan": 12,
        'amDuong': 1
    },
    {
        "id": 10,
        "chuCaiDau": "Q",
        "tenCan": "Quý",
        "nguHanh": "T",
        "nguHanhID": 3,
        "vitriDiaBan": 1,
        'amDuong': -1
    },
]


diaChi = [
    {
        "id": 0,
        "tenChi": "Hem có",
        "tenHanh": ":D",
        "amDuong": 0
    },
    {
        "id": 1,
        "tenChi": "Tý",
        "tenHanh": "T",
        "menhChu": "Tham lang",
        "thanChu": "Linh tinh",
        "amDuong": 1
    },
    {
        "id": 2,
        "tenChi": "Sửu",
        "tenHanh": "O",
        "menhChu": "Cự môn",
        "thanChu": "Thiên tướng",
        "amDuong": -1
    },
    {
        "id": 3,
        "tenChi": "Dần",
        "tenHanh": "M",
        "menhChu": "Lộc tồn",
        "thanChu": "Thiên lương",
        "amDuong": 1
    },
    {
        "id": 4,
        "tenChi": "Mão",
        "tenHanh": "M",
        "menhChu": "Văn khúc",
        "thanChu": "Thiên đồng",
        "amDuong": -1
    },
    {
        "id": 5,
        "tenChi": "Thìn",
        "tenHanh": "O",
        "menhChu": "Liêm trinh",
        "thanChu": "Văn xương",
        "amDuong": 1
    },
    {
        "id": 6,
        "tenChi": "Tỵ",
        "tenHanh": "H",
        "menhChu": "Vũ khúc",
        "thanChu": "Thiên cơ",
        "amDuong": -1
    },
    {
        "id": 7,
        "tenChi": "Ngọ",
        "tenHanh": "H",
        "menhChu": "Phá quân",
        "thanChu": "Hỏa tinh",
        "amDuong": 1
    },
    {
        "id": 8,
        "tenChi": "Mùi",
        "tenHanh": "O",
        "menhChu": "Vũ khúc",
        "thanChu": "Thiên tướng",
        "amDuong": -1
    },
    {
        "id": 9,
        "tenChi": "Thân",
        "tenHanh": "K",
        "menhChu": "Liêm trinh",
        "thanChu": "Thiên lương",
        "amDuong": 1
    },
    {
        "id": 10,
        "tenChi": "Dậu",
        "tenHanh": "K",
        "menhChu": "Văn khúc",
        "thanChu": "Thiên đồng",
        "amDuong": -1
    },
    {
        "id": 11,
        "tenChi": "Tuất",
        "tenHanh": "O",
        "menhChu": "Lộc tồn",
        "thanChu": "Văn xương",
        "amDuong": 1
    },
    {
        "id": 12,
        "tenChi": "Hợi",
        "tenHanh": "T",
        "menhChu": "Cự môn",
        "thanChu": "Thiên cơ",
        "amDuong": -1
    }
]


def ngayThangNam(nn, tt, nnnn, duongLich=True, timeZone=7):
    """Summary

    Args:
        nn (TYPE): ngay
        tt (TYPE): thang
        nnnn (TYPE): nam
        duongLich (bool, optional): bool
        timeZone (int, optional): +7 Vietnam

    Returns:
        TYPE: Description

    Raises:
        Exception: Description
    """
    thangNhuan = 0
    # if nnnn > 1000 and nnnn < 3000 and nn > 0 and \
    if nn > 0 and \
       nn < 32 and tt < 13 and tt > 0:
        if duongLich is True:
            [nn, tt, nnnn, thangNhuan] = S2L(nn, tt, nnnn, timeZone=timeZone)
        return [nn, tt, nnnn, thangNhuan]
    else:
        raise Exception("Ngày, tháng, năm không chính xác.")







def canChiNgay(nn, tt, nnnn, duongLich=True, timeZone=7, thangNhuan=False):
    """Summary

    Args:
        nn (int): ngày
        tt (int): tháng
        nnnn (int): năm
        duongLich (bool, optional): True nếu là dương lịch, False âm lịch
        timeZone (int, optional): Múi giờ
        thangNhuan (bool, optional): Có phải là tháng nhuận không?

    Returns:
        TYPE: Description
    """
    if duongLich is False:
        [nn, tt, nnnn] = L2S(nn, tt, nnnn, thangNhuan, timeZone)
    jd = jdFromDate(nn, tt, nnnn)
    # print jd
    canNgay = (jd + 9) % 10 + 1
    chiNgay = (jd + 1) % 12 + 1
    return [canNgay, chiNgay]


def canChiGio(canNgay, gio):
    """Phần này có lẽ chưa cần thiết và sẽ bổ sung sau.

    Args:
        canNgay (int): Can của ngày cần xem, 1: Giáp, 2: Ất, 3: Bính,...
        gio (int): Chi của giờ, 1: Tý, 2: Sửu,...

    Returns:
        TYPE: Description
    """
    return False


def ngayThangNamCanChi(nn, tt, nnnn, duongLich=True, timeZone=7):
    """chuyển đổi năm, tháng âm/dương lịch sang Can, Chi trong tiếng Việt.
    Không tính đến can ngày vì phải chuyển đổi qua lịch Julius.

    Hàm tìm can ngày là hàm canChiNgay(nn, tt, nnnn, duongLich=True,\
                                    timeZone=7, thangNhuan=False)

    Args:
        nn (int): Ngày
        tt (int): Tháng
        nnnn (int): Năm

    Returns:
        TYPE: Description
    """
    if duongLich is True:
        [nn, tt, nnnn, thangNhuan] = \
            ngayThangNam(nn, tt, nnnn, timeZone=timeZone)
    # Can của tháng
    canThang = (nnnn * 12 + tt + 3) % 10 + 1
    # Can chi của năm
    canNamSinh = (nnnn + 6) % 10 + 1
    chiNam = (nnnn + 8) % 12 + 1

    return [canThang, canNamSinh, chiNam]


def nguHanh(tenHanh):
    """
    Args:
        tenHanh (string): Tên Hành trong ngũ hành, Kim hoặc K, Moc hoặc M,
        Thuy hoặc T, Hoa hoặc H, Tho hoặc O

    Returns:
        Dictionary: ID của Hành, tên đầy đủ của Hành, số Cục của Hành

    Raises:
        Exception: Description
    """
    if tenHanh in ["Kim", "K"]:
        return {"id": 1, "tenHanh": "Kim", "cuc": 4, "tenCuc": "Kim tứ Cục",
                "css": "hanhKim"}
    elif tenHanh == "Moc" or tenHanh == "M":
        return {"id": 2, "tenHanh": "Mộc", "cuc": 3, "tenCuc": "Mộc tam Cục",
                "css": "hanhMoc"}
    elif tenHanh == "Thuy" or tenHanh == "T":
        return {"id": 3, "tenHanh": "Thủy", "cuc": 2, "tenCuc": "Thủy nhị Cục",
                "css": "hanhThuy"}
    elif tenHanh == "Hoa" or tenHanh == "H":
        return {"id": 4, "tenHanh": "Hỏa", "cuc": 6, "tenCuc": "Hỏa lục Cục",
                "css": "hanhHoa"}
    elif tenHanh == "Tho" or tenHanh == "O":
        return {"id": 5, "tenHanh": "Thổ", "cuc": 5, "tenCuc": "Thổ ngũ Cục",
                "css": "hanhTho"}
    else:
        raise Exception(
            "Tên Hành phải thuộc Kim (K), Mộc (M), Thủy (T), \
             Hỏa (H) hoặc Thổ (O)")


def sinhKhac(hanh1, hanh2):
    """
    Args:
        hanh1 (TYPE): Description
        hanh2 (TYPE): Description

    Returns:
        TYPE: Description
    """
    matranSinhKhac = [
        [None, None, None, None, None, None],
        [None, 0, -1, 1, -1j, 1j],
        [None, -1j, 0, 1j, 1, -1],
        [None, 1j, 1, 0, 1, -1j],
        [None, -1, 1j, -1j, 0, 1],
        [None, 1, -1j, -1, 1j, 0]
    ]
    return matranSinhKhac[hanh1][hanh2]


def nguHanhNapAm(diaChi, thienCan, xuatBanMenh=False):
    """Sử dụng Ngũ Hành nạp âm để tính Hành của năm.

    Args:
        diaChi (integer): Số thứ tự của địa chi (Tý=1, Sửu=2,...)
        thienCan (integer): Số thứ tự của thiên can (Giáp=1, Ất=2,...)

    Returns:
        Trả về chữ viết tắt Hành của năm (K, T, H, O, M)
    """
    banMenh = {
        "K1": "Hải Trung Kim",
        "T1": "Giáng Hạ Thủy",
        "H1": "Tích Lịch Hỏa",
        "O1": "Bích Thượng Thổ",
        "M1": "Tang Ðố Mộc",
        "T2": "Ðại Khê Thủy",
        "H2": "Lư Trung Hỏa",
        "O2": "Thành Ðầu Thổ",
        "M2": "Tòng Bá Mộc",
        "K2": "Kim Bạch Kim",
        "H3": "Phú Ðăng Hỏa",
        "O3": "Sa Trung Thổ",
        "M3": "Ðại Lâm Mộc",
        "K3": "Bạch Lạp Kim",
        "T3": "Trường Lưu Thủy",
        "K4": "Sa Trung Kim",
        "T4": "Thiên Hà Thủy",
        "H4": "Thiên Thượng Hỏa",
        "O4": "Lộ Bàn Thổ",
        "M4": "Dương Liễu Mộc",
        "T5": "Truyền Trung Thủy",
        "H5": "Sơn Hạ Hỏa",
        "O5": "Ðại Trạch Thổ",
        "M5": "Thạch Lựu Mộc",
        "K5": "Kiếm Phong Kim",
        "H6": "Sơn Ðầu Hỏa",
        "O6": "Ốc Thượng Thổ",
        "M6": "Bình Ðịa Mộc",
        "K6": "Xoa Xuyến Kim",
        "T6": "Ðại Hải Thủy"}

    matranNapAm = [
        [0, "G", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "N", "Q"],
        [1, "K1", False, "T1", False, "H1", False, "O1", False, "M1", False],
        [2, False, "K1", False, "T1", False, "H1", False, "O1", False, "M1"],
        [3, "T2", False, "H2", False, "O2", False, "M2", False, "K2", False],
        [4, False, "T2", False, "H2", False, "O2", False, "M2", False, "K2"],
        [5, "H3", False, "O3", False, "M3", False, "K3", False, "T3", False],
        [6, False, "H3", False, "O3", False, "M3", False, "K3", False, "T3"],
        [7, "K4", False, "T4", False, "H4", False, "O4", False, "M4", False],
        [8, False, "K4", False, "T4", False, "H4", False, "O4", False, "M4"],
        [9, "T5", False, "H5", False, "O5", False, "M5", False, "K5", False],
        [10, False, "T5", False, "H5", False, "O5", False, "M5", False, "K5"],
        [11, "H6", False, "O6", False, "M6", False, "K6", False, "T6", False],
        [12, False, "H6", False, "O6", False, "M6", False, "K6", False, "T6"]
    ]
    try:
        nh = matranNapAm[diaChi][thienCan]
        if nh[0] in ["K", "M", "T", "H", "O"]:
            if xuatBanMenh is True:
                return banMenh[nh]
            else:
                return nh[0]
    except:
        raise Exception(nguHanhNapAm.__doc__)


def dichCung(cungBanDau, *args):
    cungSauKhiDich = int(cungBanDau)
    for soCungDich in args:
        cungSauKhiDich += int(soCungDich)
    if cungSauKhiDich % 12 is 0:
        return 12
    return cungSauKhiDich % 12


def khoangCachCung(cung1, cung2, chieu=1):
    if chieu is 1:  # Con trai, chiều dương
        return (cung1 - cung2 + 12) % 12
    else:
        return (cung2 - cung1 + 12) % 12


def timCuc(viTriCungMenhTrenDiaBan, canNamSinh):
    canThangGieng = (canNamSinh * 2 + 1) % 10
    canThangMenh = ((viTriCungMenhTrenDiaBan - 3) % 12 + canThangGieng) % 10
    if canThangMenh is 0:
        canThangMenh = 10
    return nguHanhNapAm(viTriCungMenhTrenDiaBan, canThangMenh)


def timTuVi(cuc, ngaySinhAmLich):
    """Tìm vị trí của sao Tử vi

    Args:
        cuc (TYPE): Description
        ngaySinhAmLich (TYPE): Description

    Returns:
        TYPE: Description

    Raises:
        Exception: Description
    """
    cungDan = 3  # Vị trí cung Dần ban đầu là 3
    cucBanDau = cuc
    if cuc not in [2, 3, 4, 5, 6]:  # Tránh trường hợp infinite loop
        raise Exception("Số cục phải là 2, 3, 4, 5, 6")
    while cuc < ngaySinhAmLich:
        cuc += cucBanDau
        cungDan += 1  # Dịch vị trí cung Dần
    saiLech = cuc - ngaySinhAmLich
    if saiLech % 2 is 1:
        saiLech = -saiLech  # Nếu sai lệch là chẵn thì tiến, lẻ thì lùi
    return dichCung(cungDan, saiLech)


def timTrangSinh(cucSo):
    """Tìm vị trí của Tràng sinh
    Theo thứ tự cục số
    vị trí Tràng sinh sẽ là Dần, Tỵ, Thân hoặc Hợi

    *LƯU Ý* Theo cụ Thiên Lương: Nam -> Thuận, Nữ -> Nghịch

    Args:
        cucSo (int): số cục (2, 3, 4, 5, 6)

    Returns:
        int: Vị trí sao Tràng sinh

    Raises:
        Exception: Description
    """
    if cucSo == 6:  # Hỏa lục cục
        return 3  # Tràng sinh ở Dần
    elif cucSo == 4:  # Kim tứ cục
        return 6  # Tràng sinh ở Tỵ
    elif cucSo == 2 or cucSo == 5:  # Thủy nhị cục, Thổ ngũ cục
        return 9  # Tràng sinh ở Thân
    elif cucSo == 3:  # Mộc tam cục
        return 12  # Tràng sinh ở Hợi
    else:
        # print cucSo
        raise Exception("Không tìm được cung an sao Trường sinh")


def timHoaLinh(chiNamSinh, gioSinh, gioiTinh, amDuongNamSinh):
    if chiNamSinh in [3, 7, 11]:
        khoiCungHoaTinh = 2
        khoiCungLinhTinh = 4
    elif chiNamSinh in [1, 5, 9]:
        khoiCungHoaTinh = 3
        khoiCungLinhTinh = 11
    elif chiNamSinh in [6, 10, 2]:
        khoiCungHoaTinh = 11
        khoiCungLinhTinh = 4
    elif chiNamSinh in [12, 4, 8]:
        khoiCungHoaTinh = 10
        khoiCungLinhTinh = 11
    else:
        raise Exception("Không thể khởi cung tìm Hỏa-Linh")
    # print khoiCungHoaTinh, khoiCungLinhTinh

    if (gioiTinh * amDuongNamSinh) == -1:
        viTriHoaTinh = dichCung(khoiCungHoaTinh + 1, (-1) * gioSinh)
        viTriLinhTinh = dichCung(khoiCungLinhTinh - 1, gioSinh)
    elif (gioiTinh * amDuongNamSinh) == 1:
        viTriHoaTinh = dichCung(khoiCungHoaTinh - 1, gioSinh)
        viTriLinhTinh = dichCung(khoiCungLinhTinh + 1, (-1) * gioSinh)

    return [viTriHoaTinh, viTriLinhTinh]


def timThienKhoi(canNam):
    khoiViet = [None, 2, 1, 12, 10, 8, 1, 8, 7, 6, 4]
    try:
        return khoiViet[canNam]
    except:
        raise Exception("Không tìm được vị trí Khôi-Việt")


def timThienQuanThienPhuc(canNam):
    # Giáp dương Nhâm khuyển Ất long nghi
    # Mậu thổ Canh chư Quý mã thượng
    # Kỳ nhân quý hiển khả tiên tri
    thienQuan = [None, 8, 5, 6, 3, 4, 10, 12, 10, 11, 7]

    # Giáp ái kim kê Ất ái hầu
    # Đinh chư Bính thử Kỷ hổ đầu
    # Tân quý phùng xà phúc lộc nhiêu
    thienPhuc = [None, 10, 9, 1, 12, 4, 3, 7, 6, 7, 6]
    try:
        return thienQuan[canNam], thienPhuc[canNam]
    except:
        raise Exception("Không tìm được Quan-Phúc")


def timCoThan(chiNam):
    if chiNam in [12, 1, 2]:
        return 3
    elif chiNam in [3, 4, 5]:
        return 6
    elif chiNam in [6, 7, 8]:
        return 9
    else:
        return 12


def timThienMa(chiNam):
    demNghich = chiNam % 4
    if demNghich == 1:
        return 3
    elif demNghich == 2:
        return 12
    elif demNghich == 3:
        return 9
    elif demNghich == 0:
        return 6
    else:
        raise Exception("Không tìm được Thiên mã")


# Quy tắc an sao Phá Toái chuẩn (theo sách cổ như "Tử Vi Đẩu Số Toàn Thư"):
# # Tam hợp cục nào thì Phá Toái an tại cung đối xung:
# # Dần - Ngọ - Tuất → Phá Toái ở Tỵ (vì Tỵ xung Dần).
# # Thân - Tý - Thìn → Phá Toái ở Dậu (vì Dậu xung Thân).
# # Tỵ - Dậu - Sửu → Phá Toái ở Sửu (vì Sửu xung Tỵ).
# # Hợi - Mão - Mùi → Không có Phá Toái (vì không thuộc 3 cung trên).
def timPhaToai(chiNam):
    demNghich = chiNam % 3

    if demNghich == 0:
        return 10   #6
    elif demNghich == 1:
        return 6    #10
    elif demNghich == 2:
        return 2
    else:
        raise Exception("Không tìm được Phá toái")



def timTriet(canNam):
    # Giáp Kỷ, Thân Dậu cung
    if canNam in [1, 6]:
        return 9, 10

    # Ất Canh, Ngọ Mùi cung
    elif canNam in [2, 7]:
        return 7, 8

    # Bính Tân, Thìn Tị cung
    elif canNam in [3, 8]:
        return 5, 6

    # Đinh Nhâm, Dần Mão cung
    elif canNam in [4, 9]:
        return 3, 4

    # Mậu Quý, Tý Sửu cung
    elif canNam in [5, 10]:
        return 1, 2
    else:
        raise Exception("Không tìm được Triệt")


def timLuuTru(canNam):
    maTranLuuHa = [None, 10, 11, 8, 5, 6, 7, 9, 4, 12, 3]
    maTranThienTru = [None, 6, 7, 1, 6, 7, 9, 3, 7, 10, 11]
    try:
        return maTranLuuHa[canNam], maTranThienTru[canNam]
    except:
        raise Exception("Không tìm được Lưu - Trù")


def canChiNam(namDL):
    can_id = (namDL + 6) % 10 + 1
    chi_id = (namDL + 8) % 12 + 1

    canTen = next((c['tenCan'] for c in thienCan if c['id'] == can_id), None)
    chiTen = next((c['tenChi'] for c in diaChi if c['id'] == chi_id), None)

    return {
        "nam": namDL,
        "can": can_id,
        "chi": chi_id,
        "canTen": canTen,
        "chiTen": chiTen
    }

# Thiên can năm – Dương: Giáp, Bính, Mậu, Canh, Nhâm (0,2,4,6,8)
DUONG_CAN = ["Giáp", "Bính", "Mậu", "Canh", "Nhâm"]
AM_CAN = ["Ất", "Đinh", "Kỷ", "Tân", "Quý"]
# Tháng và ngày – số lẻ: dương | số chẵn: âm
def is_duong_so(n): return n % 2 == 1
# Giờ âm/dương theo 12 Địa Chi
DUONG_GIO = ["Tý", "Dần", "Thìn", "Ngọ", "Thân", "Tuất"]
AM_GIO = ["Sửu", "Mão", "Tỵ", "Mùi", "Dậu", "Hợi"]

def tinh_am_duong_nam(can_nam):  # ví dụ: "Giáp"
    return "Dương" if can_nam in DUONG_CAN else "Âm"

def tinh_am_duong_thang(thang):  # tháng: 1–12
    return "Dương" if is_duong_so(thang) else "Âm"

def tinh_am_duong_ngay(ngay):  # ngày: 1–31
    return "Dương" if is_duong_so(ngay) else "Âm"

def tinh_am_duong_gio(gio_chi):  # ví dụ: "Tý"
    return "Dương" if gio_chi in DUONG_GIO else "Âm"

def xac_dinh_am_duong_thuan_nghich_ly(can_nam, thang, ngay, gio_chi):
    # Tính âm/dương của từng yếu tố
    nam_ad = tinh_am_duong_nam(can_nam)
    thang_ad = tinh_am_duong_thang(thang)
    ngay_ad = tinh_am_duong_ngay(ngay)
    gio_ad = tinh_am_duong_gio(gio_chi)

    # So sánh cặp: năm – tháng | ngày – giờ
    match1 = nam_ad == thang_ad
    match2 = ngay_ad == gio_ad

    # Kết luận
    if match1 and match2:
        return "Âm dương thuận lý"
    else:
        return "Âm dương nghịch lý"




def tinh_can_luong_bat_tu(canNamTen, chiNamTen, thangAm, ngayAm, chiGioTen):
    # 1. Giờ sinh
    gio_map = {
        "Tý": 1.6, "Sửu": 0.6, "Dần": 0.7, "Mão": 1.0, "Thìn": 0.9, "Tỵ": 1.6,
        "Ngọ": 1.0, "Mùi": 0.8, "Thân": 0.8, "Dậu": 0.9, "Tuất": 0.6, "Hợi": 0.6
    }

    # 2. Ngày sinh
    ngay_map = {
        1: 0.5, 2: 1.0, 3: 0.8, 4: 1.5, 5: 1.6, 6: 1.5, 7: 0.8, 8: 1.6,
        9: 0.8, 10: 1.6, 11: 0.9, 12: 1.7, 13: 0.8, 14: 1.7, 15: 1.0, 16: 0.8,
        17: 0.9, 18: 1.8, 19: 0.5, 20: 1.5, 21: 1.0, 22: 0.9, 23: 0.8, 24: 0.9,
        25: 1.5, 26: 1.8, 27: 0.7, 28: 0.8, 29: 1.6, 30: 0.6
    }

    # 3. Tháng sinh
    thang_map = {
        1: 0.6, 2: 0.7, 3: 1.8, 4: 0.9, 5: 0.5, 6: 1.6, 7: 0.9, 8: 1.5,
        9: 1.8, 10: 1.8, 11: 0.9, 12: 0.5
    }

    # 4. Năm sinh (can + chi)
    nam_map = {
        "Giáp Tý": 1.2, "Bính Tý": 1.6, "Mậu Tý": 1.5, "Canh Tý": 0.7, "Nhâm Tý": 0.5,
        "Ất Sửu": 0.9, "Đinh Sửu": 0.8, "Kỷ Sửu": 0.8, "Tân Sửu": 0.7, "Quý Sửu": 0.5,
        "Bính Dần": 0.6, "Mậu Dần": 0.8, "Canh Dần": 0.9, "Nhâm Dần": 0.9, "Giáp Dần": 1.2,
        "Đinh Mão": 0.7, "Kỷ Mão": 1.9, "Tân Mão": 1.2, "Quý Mão": 1.2, "Ất Mão": 0.8,
        "Mậu Thìn": 1.2, "Canh Thìn": 1.2, "Nhâm Thìn": 1.0, "Giáp Thìn": 0.8, "Bính Thìn": 0.8,
        "Kỷ Tỵ": 0.5, "Tân Tỵ": 0.6, "Quý Tỵ": 0.7, "Ất Tỵ": 0.7, "Đinh Tỵ": 0.6,
        "Canh Ngọ": 0.9, "Nhâm Ngọ": 0.8, "Giáp Ngọ": 1.5, "Bính Ngọ": 1.3, "Mậu Ngọ": 1.9,
        "Tân Mùi": 0.8, "Quý Mùi": 0.7, "Ất Mùi": 0.6, "Đinh Mùi": 0.5, "Kỷ Mùi": 0.6,
        "Nhâm Thân": 0.7, "Giáp Thân": 0.5, "Bính Thân": 0.5, "Mậu Thân": 1.4, "Canh Thân": 0.8,
        "Quý Dậu": 0.8, "Ất Dậu": 1.5, "Đinh Dậu": 1.4, "Kỷ Dậu": 0.5, "Tân Dậu": 1.6,
        "Giáp Tuất": 0.5, "Bính Tuất": 0.6, "Mậu Tuất": 1.4, "Canh Tuất": 0.9, "Nhâm Tuất": 1.0,
        "Ất Hợi": 0.9, "Đinh Hợi": 1.6, "Kỷ Hợi": 0.9, "Tân Hợi": 1.7, "Quý Hợi": 0.7
    }

    # Tính tổng cân lượng
    gio = gio_map.get(chiGioTen, 0)
    ngay = ngay_map.get(ngayAm, 0)
    thang = thang_map.get(thangAm, 0)
    nam = nam_map.get(f"{canNamTen} {chiNamTen}", 0)
    tong = gio + ngay + thang + nam

    return round(tong, 2)  # Làm tròn 2 chữ số sau dấu phẩy

def format_can_luong(value):
    luong = int(value)
    chi = int(round((value - luong) * 10))
    return f"{luong} lượng {chi} chỉ"


def binh_giai_can_luong(can_luong_float):
    # Làm tròn 1 chữ số thập phân để khớp key
    key = round(can_luong_float, 1)
    return dict_binh_giai_can_luong.get(key, "Không tìm thấy bình giải cho số cân lượng này.")



dict_binh_giai_can_luong = {
    7.1: "Sinh ra với số mệnh phi thường, được ban cho nhiều khanh tướng công hầu, sống trong sự tiêu diêu khoái lạc của phúc báo. Cuộc sống của họ tràn đầy vinh hoa và phú quý, thu hút sự kính trọng của mọi người xung quanh.",
    7.0: "Ở cân lượng chỉ trong tử vi này họ được phúc lớn như biển, không phải lo lắng gì cả. Y lộc và tài vận do trời ban cho không thể thay đổi, mang lại một đời sống vinh quang và phú quý không ai sánh kịp.",
    6.9: "Số này đại diện cho một ngôi sao may mắn trên trần gian. Họ sẽ có một thân giàu sang phú quý, được tôn trọng và ngưỡng mộ. Phước lộc này được xem là do trời ban tặng, mang lại hạnh phúc và vinh hiển suốt cuộc đời.",
    6.8: "Người này có phú quý do trời phú cho, không cần vất vả nhiều, và gia sản của họ có đầy ắp. Tuy nhiên, sau một khoảng thời gian, sự phồn thịnh có thể giảm đi và phước lộc tổ tiên tan biến như chiếc thuyền giữa biển cả giông tố.",
    6.7: "Sinh ra đã được trời ban phước báo, với ruộng đất và gia sản thịnh vượng. Họ sẽ trải qua một cuộc sống giàu sang và an lành, đồng thời được kính trọng và yêu mến.",
    6.6: "Số này đồng nghĩa với phú quý do trời sắp đặt sẵn. Họ sẽ vươn lên vượt qua mọi người, đạt được quan vị cao sang và uy quyền, với châu báu ngập tràn và sự sung sướng trong mọi khía cạnh cuộc sống.",
    6.5: "Người này mang đến phước lộc không ít, có tài năng giúp ích cho cộng đồng, và có chức tước cao quý trong triều đình. Cuộc sống của họ đầy đủ về tài chính và danh tiếng, được tôn vinh và kính trọng khắp nơi.",
    6.4: "Số này biểu thị giàu sang vinh diệu không ai sánh bằng. Họ sẽ có uy quyền và quyền lực, ngồi ở vị trí cao nhất trong triều đình, và trải qua cuộc sống sung sướng và vui vẻ suốt đời.",
    6.3: "Số này là số thi đỗ cao cấp, làm quan trọng, giàu sang vô cùng. Được khen ngợi và tôn trọng, họ sẽ trải qua một cuộc sống an nhàn và viên mãn, với phúc lộc vô biên và gia đình hưng thịnh.",
    6.2: "Người này sẽ có phước lộc không tận, học tập thành tài, làm cho cha mẹ tự hào. Với áo gấm và đai vàng, họ sẽ sống một cuộc sống giàu có và phồn thịnh, với sự sung túc bền vững.",
    6.1: "Người có cân lượng chỉ trong tử vi với số này sở hữu trí tuệ sáng suốt, chăm chỉ học tập và tự thân vinh quang. Tên tuổi của họ được ghi vào bảng danh dự, và mặc dù không nắm giữ vị trí quan cao, nhưng chắc chắn sẽ là một người giàu có.",
    6.0: "Số này là của người có tên ghi vào bảng cao nhất, xây dựng công danh to lớn, tạo ra vinh hiển cho gia tộc. Ruộng đất và gia sản của họ thịnh vượng, sức khỏe dồi dào, đánh dấu một cuộc sống đầy đủ.",
    5.9: "Người có số này là người tài năng xuất chúng, với thân thể mềm mại và linh hồn thanh khiết. Phận trời ban cho họ học vấn cao siêu, đạt được thành công trong các kỳ thi danh giá, và được phong quan tước chức cao quý.",
    5.8: "Số này đại diện cho người giàu sang phú quý, được trời ưu ái ban phước lộc suốt đời. Họ sống một cuộc sống an nhàn và sung túc, với danh vọng kiêu ngạo, tài lộc dồi dào và phú thọ viên mãn.",
    5.7: "Người có số này hưởng phước trọn vẹn, mọi việc đều thuận lợi. Quang vinh của tổ tiên tiếp tục tỏa sáng, tạo nên một cuộc sống oai hùng và tự tại. Họ được mọi người kính trọng và yêu mến.",
    5.6: "Số này là của người hiếu đạo thông minh, đảm bảo cuộc đời an khang phước đức. Trải qua nhiều thăng trầm, họ sở hữu nguồn tài lợi vô biên, mang lại bình an và hậu duệ.",
    5.5: "Số này ám chỉ cuộc sống trẻ trung đầy khó khăn trên con đường danh vọng, nhưng vận may đưa họ vượt qua mọi chông gai. Phước lộc sẽ ùa về như nước triều dâng, khiến cuộc sống giàu có và vinh quang.",
    5.4: "Số này là của người có tính cách chính trực và cao thượng, học tập chăm chỉ, ăn mặc thanh lịch, và sẽ sống một cuộc sống an bình. Họ là những người có phúc khí trên đời.",
    5.3: "Người có số này thường được đánh giá là tính tình chân thành, đồng thời công việc gia đình thành công là nhờ vào đó. Phước lộc suốt đời đã được sắp đặt, mang đến họ một cuộc sống phú quý.",
    5.2: "Cuộc đời hạnh phúc, mọi việc tốt lành và yên vui. Họ hàng thân thuộc luôn ủng hộ, và sự thăng tiến trong sự nghiệp là điều hiển nhiên.",
    5.1: "Số này mang đến cuộc sống rực rỡ, mọi thứ thuận buồm xuôi gió. Không cần gắng sức mà họ sẽ tự nhiên hạnh phúc. Gia sản và phước lộc trọn vẹn.",
    5.0: "Số này thường chỉ việc lo lắng về công danh và tài lợi mỗi ngày. Đến khi già, họ sẽ được hưởng cuộc sống nhàn hạ, đặc biệt nếu có vì sao Tài Tinh chiếu sáng.",
    4.9: "Đây là số của phúc lộc vô biên, do chính tay gầy dựng sự nghiệp vinh quang cho gia đình. Người giàu có đều kính nể, và cuộc sống của họ đầy hạnh phúc.",
    4.8: "Số này biểu thị cuộc đời khó khăn, từ khi trẻ đến già, nhưng với chút an ổn khi già. Anh em họ hàng không thể giúp đỡ nhiều, nhưng ít nhất họ sẽ có một giai đoạn cuộc sống tương đối ổn định.",
    4.7: "Người này sẽ trải qua giau sang khi tuổi già, với vợ con phú quý, nhờ vào việc tích lũy phước báu như nước chảy về.",
    4.6: "Số này là của những người may mắn ở mọi nơi, đặc biệt là khi thay đổi họ hoặc dời nhà. Ăn mặc no đủ do số trời ban. Từ nửa đời trở đi, họ sẽ có một cuộc sống ổn định và bình an.",
    4.5: "Cuộc sống của người này đầy khó khăn về công danh và lợi lộc. Trước đó, họ phải chịu đựng nhiều khổ cực, sau đó có những khoảnh khắc may mắn. Số ít con cái và anh em ruột cũng không đóng góp nhiều.",
    4.4: "Số này là của những người được trời ban phước lộc, không cần lo lắng quá nhiều. Phúc lộc sẽ tăng lên rất nhiều sau này. Dù có khó khăn khi trẻ, nhưng khi già, họ sẽ được tận hưởng cuộc sống an bình.",
    4.3: "Số này ám chỉ người thông minh và tài năng, tự tin trước mọi người. Phước lộc do trời ban, không cần vất vả nhiều mà mọi việc đều suôn sẻ.",
    4.2: "Số này mang lại nhiều điều mà nhiều người mong đợi. Từ nửa đời trở đi, vận mệnh sẽ tốt hơn, và tài lộc công danh sẽ phát triển mạnh mẽ.",
    4.1: "Số này đại diện cho sự tài ba nhưng không ổn định. Cuộc sống làm việc đa dạng, không giống nhau. Từ nửa đời trở đi, sự suy thoái phước tiêu diêu khiến cuộc sống không còn như xưa, chưa thành công như mong đợi.",
    4.0: "Số này biểu thị một cuộc sống phúc lộc bền vững, mặc dù trước đó phải trải qua nhiều thách thức và khó khăn. Tuy nhiên, sau này sẽ hưởng thụ cuộc sống an nhàn và giàu có.",
    3.9: "Đường đời gian nan và trắc trở. Dù có cố gắng, thành công vẫn khó khăn. Những nỗ lực xây dựng sự nghiệp cuối cùng tan thành mây khói.",
    3.8: "Tính tình cao thượng, và từ 36 tuổi trở đi, may mắn sẽ đến. Sự giàu sang và phú quý, cùng với sự ngưỡng mộ và kính trọng từ người khác, sẽ là đỉnh cao của cuộc đời.",
    3.7: "Không có duyên với công việc, và không có sự giúp đỡ từ anh em thân thuộc. Cuộc sống chỉ có thể tồn tại nhờ vào gia sản của tổ tiên, nhưng không bền lâu. Khi đi xa, không biết khi nào mới có thể trở về.",
    3.6: "Toàn bộ cuộc đời không cần phải vất vả quá mức, chỉ cần kiểm soát được tình hình. Có phúc khí lớn, giúp vượt qua mọi khó khăn. Sẽ có tài lộc và hạnh phúc trong cuộc sống.",
    3.5: "Phúc đức không hoàn thiện, không được hưởng trọn vẹn như phước lộc của tổ tiên. Cần chờ đợi thời cơ mới có thể cải thiện tình hình và đạt được sự no đủ hơn.",
    3.4: "Có phúc khí từ việc tu tập và tìm đến chỗ Phật. Niệm Phật hàng ngày là nguồn an lành và viên mãn.",
    3.3: "Đầu đời khó khăn trong việc thành công, và mưu tính không hiệu quả. Từ nửa đời trở đi, vận may sẽ tốt hơn, mang theo tài lộc phát triển.",
    3.2: "Gặp nhiều rủi ro khi trẻ, nhưng sau này tài lợi sẽ chảy về như nước. Nửa sau cuộc đời sẽ đầy ắp sung túc, với công danh và lợi lộc thuận buồm xuôi gió.",
    3.1: "Sinh ra trong kế gian khổ và vất vả, khó có thể dựa vào gia sản của tổ tiên để xây dựng nhà cửa. Chỉ từ nửa sau cuộc đời mới có đủ ăn đủ mặc.",
    3.0: "Lao lực suốt đời, với sự khổ sở và chăm chỉ kiếm tiền. Đến khi già, chỉ có thể giảm bớt chút phiền muộn.",
    2.9: "Ngày xưa vất vả với cuộc sống, không có duyên nợ để thành công sớm. Công danh đến chậm chạp, và phải đến 40 tuổi mới có được cuộc sống yên bình. Có thể cần thay đổi nơi ở hoặc họ tên để đạt được may mắn.",
    2.8: "Làm ăn bừa bãi, không có tổ chức, và sản nghiệp của tổ tiên như một giấc mơ xa vời. Nếu không nhận làm con nuôi hoặc không đổi họ tên, chắc chắn phải di cư nhiều lần trong đời.",
    2.7: "Tự lo toan suốt đời, khó gặp được sự giúp đỡ, và không thể dựa vào phúc đức của tổ tiên để vững vàng. Tự lực cánh sinh quanh năm, từ nhỏ đến già cũng không có gì đáng nhớ.",
    2.6: "Số phận khốn khổ, vật lộn một mình với cuộc sống. Phải rời xa quê hương để kiếm sống, có lẽ chỉ khi già mới có chút an nhàn.",
    2.5: "Số này do tổ nghiệp suy yếu, khó có thể xây dựng gia đình hạnh phúc. Họ hàng thân thích gặp nhiều phiền toái, và cuộc đời khổ cực, chỉ biết tự lo cho bản thân.",
    2.4: "Không có phúc lộc trong gia đình, khó thành công trong sự nghiệp, và không có sự giúp đỡ từ họ hàng. Phải lang thang khắp nơi để kiếm sống tới khi già.",
    2.3: "Dù cố gắng làm việc, nhưng khó thành công, không có sự ủng hộ của anh em họ hàng. Cuối cùng, chỉ biết chịu số phận và đi xa quê hương để tìm kiếm miếng cơm manh áo.",
    2.2: "Số này do thân hàn cốt lạnh, khổ não tận tâm can, lo toan kiếm ăn trong nghèo khó. Nếu không cẩn thận, có thể trở thành kẻ lang thang do số mệnh quyết định."
    }