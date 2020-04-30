class LevelColor(object):
    # source: https://meatfighter.com/nintendotetrisai/#Coloring_Tetriminos
    # fmt: off
    DATA = [
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x03, 0x61, 0x21], [0x03, 0x72, 0x61],
            [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31], [0x62, 0x92, 0x52], [0x90, 0x41, 0x03],
            [0x92, 0x02, 0x50], [0x62, 0x90, 0x52], [0x90, 0x41, 0x03], [0x92, 0x02, 0x50], [0x02, 0x52, 0x90], [0x02, 0x03, 0x61], [0xd0, 0x90, 0x10], [0x02, 0x52, 0x42], [0x00, 0x01, 0xd0], [0x42, 0x52, 0x73],
            [0x52, 0x02, 0xb2], [0x50, 0x62, 0xc0], [0x81, 0x52, 0x52], [0x73, 0x01, 0x63], [0x42, 0x90, 0xc1], [0x03, 0x92, 0x00], [0x42, 0x50, 0x50], [0x10, 0x92, 0x10], [0x80, 0x92, 0x50], [0x00, 0x62, 0xd0],
            [0x61, 0x91, 0x50], [0x02, 0x92, 0x91], [0xd0, 0x90, 0x10], [0x70, 0x52, 0x62], [0xd0, 0xc0, 0x62], [0x02, 0xb2, 0x81], [0xd0, 0x92, 0x00], [0xd0, 0x02, 0x52], [0x90, 0x50, 0x01], [0x62, 0x31, 0x62],
            [0xd3, 0x00, 0xd0], [0xa0, 0xa0, 0xa0], [0x70, 0xa2, 0xd3], [0x91, 0x02, 0x02], [0x91, 0x02, 0x62], [0x52, 0x71, 0x81], [0xa1, 0x92, 0x70], [0x70, 0x03, 0x80], [0xd3, 0xd0, 0x91], [0x91, 0x01, 0xc1],
            [0x71, 0x02, 0x20], [0x70, 0xb2, 0x52], [0x92, 0x70, 0x81], [0x91, 0x90, 0x70], [0x60, 0x83, 0x92], [0xc0, 0xa2, 0x91], [0xd3, 0xd0, 0x91], [0x91, 0x02, 0x00], [0x00, 0x00, 0x10], [0x10, 0x10, 0x20],
            [0x30, 0x40, 0x40], [0x50, 0x50, 0x50], [0x03, 0x12, 0x21], [0x03, 0x92, 0xa1], [0x03, 0x42, 0x41], [0x03, 0xa2, 0x21], [0x03, 0xb2, 0x51], [0x03, 0x22, 0xb2], [0x03, 0x00, 0x61], [0x03, 0x50, 0x31],
            [0x03, 0x61, 0x21], [0x03, 0x72, 0x61], [0x62, 0x92, 0x52], [0x90, 0x41, 0x03], [0x92, 0x02, 0x50], [0x62, 0x90, 0x52], [0x90, 0x41, 0x03], [0x92, 0x02, 0x50], [0x02, 0x52, 0x90], [0x02, 0x03, 0x61],
            [0xd0, 0x90, 0x10], [0x02, 0x52, 0x42], [0x00, 0x01, 0xd0], [0x42, 0x52, 0x73], [0x52, 0x02, 0xb2], [0x50, 0x62, 0xc0], [0x81, 0x52, 0x52], [0x73, 0x01, 0x63], [0x42, 0x90, 0xc1], [0x03, 0x92, 0x00],
            [0x42, 0x50, 0x50], [0x10, 0x92, 0x10], [0x80, 0x92, 0x50], [0x00, 0x62, 0xd0], [0x61, 0x91, 0x50], [0x02, 0x92, 0x91], [0xd0, 0x90, 0x10], [0x70, 0x52, 0x62], [0xd0, 0xc0, 0x62], [0x02, 0xb2, 0x81],
            [0xd0, 0x92, 0x00], [0xd0, 0x02, 0x52], [0x90, 0x50, 0x01], [0x62, 0x31, 0x62], [0xd3, 0x00, 0xd0], [0xa0, 0xa0, 0xa0], [0x70, 0xa2, 0xd3], [0x91, 0x02, 0x02], [0x91, 0x02, 0x62], [0x52, 0x71, 0x81],
            [0xa1, 0x92, 0x70], [0x70, 0x03, 0x80], [0xd3, 0xd0, 0x91], [0x91, 0x01, 0xc1], [0x71, 0x02, 0x20], [0x70, 0xb2, 0x52], [0x92, 0x70, 0x81], [0x91, 0x90, 0x70], [0x60, 0x83, 0x92], [0xc0, 0xa2, 0x91],
            [0xd3, 0xd0, 0x91], [0x91, 0x02, 0x00], [0x00, 0x00, 0x10], [0x10, 0x10, 0x20], [0x30, 0x40, 0x40], [0x50, 0x50, 0x50]
           ]
    # fmt: on

    def __init__(self, palette):
        self.palette = palette

    def get_colors(self, level):
        indices = self.DATA[level]
        print(indices)
        return [self.palette.get_color(index) for index in indices]
