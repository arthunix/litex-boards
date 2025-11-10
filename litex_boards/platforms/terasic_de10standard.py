#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2019 Antony Pavlov <antonynpavlov@gmail.com>
# Copyright (c) 2025 Arthur Silverio <thursilverio@gmail.com>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform
from litex.build.altera.programmer import USBBlaster

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk50", 0, Pins("AF14"), IOStandard("3.3-V LVTTL")),
    ("clk50", 1, Pins("AA16"), IOStandard("3.3-V LVTTL")),
    ("clk50", 2, Pins("Y26"),  IOStandard("3.3-V LVTTL")),
    ("clk50", 3, Pins("K14"),  IOStandard("3.3-V LVTTL")),

    # Leds
    ("user_led", 0, Pins("AA24"), IOStandard("3.3-V LVTTL")),
    ("user_led", 1, Pins("AB23"), IOStandard("3.3-V LVTTL")),
    ("user_led", 2, Pins("AC23"), IOStandard("3.3-V LVTTL")),
    ("user_led", 3, Pins("AD24"), IOStandard("3.3-V LVTTL")),
    ("user_led", 4, Pins("AG25"), IOStandard("3.3-V LVTTL")),
    ("user_led", 5, Pins("AF25"), IOStandard("3.3-V LVTTL")),
    ("user_led", 6, Pins("AE24"), IOStandard("3.3-V LVTTL")),
    ("user_led", 7, Pins("AF24"), IOStandard("3.3-V LVTTL")),
    ("user_led", 8, Pins("AB22"), IOStandard("3.3-V LVTTL")),
    ("user_led", 9, Pins("AC22"), IOStandard("3.3-V LVTTL")),

    # Seven Segment
    ("seven_seg", 0, Pins("W17 V18 AG17 AG16 AH17 AG18 AH18"), IOStandard("3.3-V LVTTL")),
    ("seven_seg", 1, Pins("AF16 V16 AE16 AD17 AE18 AE17 V17"), IOStandard("3.3-V LVTTL")),
    ("seven_seg", 2, Pins("AA21 AB17 AA18 Y17 Y18 AF18 W16"), IOStandard("3.3-V LVTTL")),
    ("seven_seg", 3, Pins("Y19 W19 AD19 AA20 AC20 AA19 AD20"), IOStandard("3.3-V LVTTL")),
    ("seven_seg", 4, Pins("AD21 AG22  AE22 AE23 AG23 AF23 AH22"), IOStandard("3.3-V LVTTL")),
    ("seven_seg", 5, Pins("AF21 AG21 AF20 AG20 AE19 AF19 AB21"), IOStandard("3.3-V LVTTL")),

    # Button
    ("key", 0, Pins("AJ4"), IOStandard("3.3-V LVTTL")),
    ("key", 1, Pins("AK4"), IOStandard("3.3-V LVTTL")),
    ("key", 2, Pins("AA14"),  IOStandard("3.3-V LVTTL")),
    ("key", 3, Pins("AA15"),  IOStandard("3.3-V LVTTL")),

    # Switches
    ("user_sw", 0, Pins("AB30"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 1, Pins("Y27"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 2, Pins("AB28"),  IOStandard("3.3-V LVTTL")),
    ("user_sw", 3, Pins("AC30"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 4, Pins("W25"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 5, Pins("V25"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 6, Pins("AC28"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 7, Pins("AD30"),  IOStandard("3.3-V LVTTL")),
    ("user_sw", 8, Pins("AC29"), IOStandard("3.3-V LVTTL")),
    ("user_sw", 9, Pins("AA30"), IOStandard("3.3-V LVTTL")),

    # Serial
    ("serial", 0,
        Subsignal("tx", Pins("W15"), IOStandard("3.3-V LVTTL")),
        Subsignal("rx", Pins("AK2"), IOStandard("3.3-V LVTTL"))
    ),

    # I2C
    ("i2c", 0,
        Subsignal("sclk", Pins("Y24")),
        Subsignal("sdat", Pins("Y23")),
        IOStandard("3.3-V LVTTL")
    ),

    # VGA
    ("vga", 0,
        Subsignal("hsync_n", Pins("AK19")),
        Subsignal("vsync_n", Pins("AK18")),
        Subsignal("r", Pins("AK29 AK28 AK27 AJ27 AH27 AF26 AG26 AJ26")),
        Subsignal("g", Pins("AK26 AJ25 AH25 AK24 AJ24 AH24 AK23 AH23")),
        Subsignal("b", Pins("AJ21 AJ20 AH20 AJ19 AH19 AJ17 AJ16 AK16")),
        IOStandard("3.3-V LVTTL")
    ),

    # GPIOs
    ("gpio_0", 0,
        Pins("W15 AK2 Y16 AK3 AJ1 AJ2 AH2 AH3 AH4 AH5 AG1 AG2 AG3 AG5 AG6 AG7 AG8 AF4 AF5 AF6 AF8 AF9 AF10 AE7 AE9 AE11 AE12 AD7 AD9 AD10 AD11 AD12 AC9 AC12 AB12 AA12"),
        IOStandard("3.3-V LVTTL")
    ),

    # SDR SDRAM
    ("sdram_clock", 0, Pins("AH12"), IOStandard("3.3-V LVTTL")),
    ("sdram", 0,
        Subsignal("a",     Pins(
            "AK14 AH14 AG15 AE14 AB15 AC14 AD14 AF15",
            "AH15 AG13 AG12 AH13 AJ14")),
        Subsignal("ba",    Pins("AF13 AJ12")),
        Subsignal("cs_n",  Pins("AG11")),
        Subsignal("cke",   Pins("AK13")),
        Subsignal("ras_n", Pins("AE13")),
        Subsignal("cas_n", Pins("AF11")),
        Subsignal("we_n",  Pins("AA13")),
        Subsignal("dq", Pins(
            "AK6 AJ7 AK7 AK8 AK9 AG10 AK11 AJ11",
            "AH10 AJ10 AJ9 AH9 AH8 AH7 AJ6 AJ5")),
        Subsignal("dm", Pins("AB13 AK12")),
        IOStandard("3.3-V LVTTL")
    ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name   = "clk50"
    default_clk_period = 1e9/50e6

    def __init__(self, toolchain="quartus"):
        AlteraPlatform.__init__(self, "5CSXFC6D6F31C6", _io, toolchain=toolchain)

    def create_programmer(self):
        return USBBlaster(cable_name="DE-SoC", device_id=2)

    def do_finalize(self, fragment):
        AlteraPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk50", loose=True), 1e9/50e6)
