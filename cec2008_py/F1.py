#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 12:29, 20/04/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieunguyen5991                                                  %
#-------------------------------------------------------------------------------------------------------%

from opfunu.cec.cec2008.root import Root
from numpy import sum


class Model(Root):
    def __init__(self, f_name="Shifted Sphere Function", f_shift_data_file="schwefel_shift_func_data", f_ext='.txt', f_bias=-450):
        Root.__init__(self, f_name, f_shift_data_file, f_ext, f_bias)

    def _main__(self, solution=None):
        problem_size = len(solution)
        if problem_size > 1000:
            print("CEC 2008 not support for problem size > 1000")
            return 1
        shift_data = self.load_shift_data()[:problem_size]
        return sum((solution - shift_data)**2) + self.f_bias











