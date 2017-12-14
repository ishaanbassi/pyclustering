/**
*
* Copyright (C) 2014-2017    Andrei Novikov (pyclustering@yandex.ru)
*
* GNU_PUBLIC_LICENSE
*   pyclustering is free software: you can redistribute it and/or modify
*   it under the terms of the GNU General Public License as published by
*   the Free Software Foundation, either version 3 of the License, or
*   (at your option) any later version.
*
*   pyclustering is distributed in the hope that it will be useful,
*   but WITHOUT ANY WARRANTY; without even the implied warranty of
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*   GNU General Public License for more details.
*
*   You should have received a copy of the GNU General Public License
*   along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
*/


#pragma once


namespace ccore {

namespace utils {

namespace random {


/**
 *
 * @brief   Returns random value using specified mean and deviation using normal distribution.
 *
 * @param[in] p_mean: Mean.
 * @param[in] p_dev:  Standard deviation.
 *
 * @return  Returns random variable.
 *
 */
double generate_normal_random(const double p_mean = 0.0, const double p_dev = 1.0);


}

}

}