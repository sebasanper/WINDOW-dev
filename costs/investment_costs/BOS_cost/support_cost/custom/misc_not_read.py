# from turbine_description import rotor_radius
# ------------------------------------------------------- GENERAL NOTES --------------------------------------------------------------------------------
# Some variables/inputs are used twice with a different name due to the fact that 3 different algorithms were combined and
# thus different approaches were used.
# So the user must change these inputs twice !!!!
rotor_radius = 40.0
hub_height = 80.0
# ----------------------------------------------------------- INPUTS ----------------------------------------------------------------------------------
Delta = 0.5  # m/s. Delta is the size of the wind speed bins
k = 0.04  # Decay constant
r0 = 40.0  # Turbine rotor radius
# ----------------------------------------------------- Support Structure - INPUTS ----------------------------------------------------------------------
# Properties
solidity_rotor = 0.052  # [-] 'Generic' value, based on Peter Jamieson's book - Figure 2.5 - P.53
cd_rotor_idle_vane = 0.4  # [-] 'Generic' value, very dependent on angle of attack and therefore the assumed rotor misalignment
# cd_rotor_idle_failed_pitch = 1.2 # [-]
cd_nacelle = 1.2  # [-] OWTES V66: 1.3, but using a frontal area of 13 m^2
front_area_nacelle = 14.0  # [m^2] Vestas V80 brochure: height for transport 4 m, width 3.4 m, rounded up 14 m^2 to include height including cooler top 5.4 m
max_thrust = 475000.0  # [N] Maximum thrust determined from thrust coefficient curve multiplied with 1.5 amplification factor (determined by Otto for NREL 5 MW turbine)
yaw_to_hub_height = 2.0  # [m] Vestas V80 brochure: height for transport 4 m - On picture, the axis appears to be in the middle of the nacelle.
mass = 98500.0  # [kg] 79 tonne nacelle + 3x 6.5 tonne blades
mass_eccentricity = -2.0  # [m] - in x-direction, so negative when upwind of tower centre - Just a guess - Vestas V80 brochure: Length of nacelle = 10.4 m
yaw_diameter = 2.26  # [m] From OWTES V66
wind_speed_at_max_thrust = 12.0  # [m/s] Horns rev website: 13 m/s - Vestas V80 brochure: 16 m/s, but max thrust appears at 12 m/s
generator_voltage = 690.0  # [V] There are 480 and 690 voltage versions of the V80. The higher voltage is assumed, considering the need of high voltage in the connections to the public grid.
pm_interval = 4380.0  # [h] Horns Rev website: two services per year
pm_duration = 23.0  # [h] (Spare parts report: 1x 3 days, 1x 2 days. 1 day = 12 hours minus ~3 hours preparation and sailing (2x 2 hours are mentioned for CM, but during PM an extra boat is available): average: 2.5 * 9 hours)
pm_consumables_costs = 1250.0  # [E] (Spare parts report: 1x 1500, 1x 1000 Euro; Average: 1250 Euro)
people_per_crew = 3  # [-] (Spare part optimisation report p.52: 6 Vattenfall technicians in 1 shift, with 3 Vestas service personnel, so probably 2 Vattenfall and 1 Vestas people per crew - For PM 2 technicians are needed)
purchase_price = 1500000.0  # [Euro]
warranty_percentage = 15.0  # [%]

# Physical Environment
scale_factor = 10.83  # [m/s] Horns Rev website: Data fitted, resulting in average wind speed of 9.6, which is close to given value of 9.7
shape_factor = 2.35  # [-] Horns Rev website: Data fitted, resulting in average wind speed of 9.6, which is close to given value of 9.7
ref_height_wind_speed = 62.0
alpha = 0.10  # Approximate mean value of fits to data in ECN report and paper of Tambke (EWEC 2004)
hat = 0.8  # Horns Rev website: Tides are approximately 1.2 m; Paper ICCE: appr. 1.5 m - A little more than half of this is taken for 'extrapolation'
lat = -0.8  # Horns Rev website: Tides are approximately 1.2 m; Paper ICCE: appr. 1.5 m - A little more than half of this is taken for 'extrapolation'
storm_surge_pos = 2.5  # Paper ICCE
storm_surge_neg = -0.5  # Guess
Hs_50_year = 5.0  # Horns Rev website: Highest value in graph of Hm0 is 4.3. Somewhat higher value taken for 'extrapolation' (note: graph is for 1 hour values) - Support structure design tool description derives Hs_1_year = 0.64 * Hs_50_year
Hs_1_year = 3.3  # Horns Rev website: waves of more than 6 m height reached every year. Divided by 1.86 to estimate significant wave height
current_depth_averaged_50_year = 0.8  # [m/s] Horns Rev website: Currents may reach 0.8 m/s during storms (doesn't mention return period and whether this is depth averaged)
angle_wave_current_50_year = 20.0  # [degrees] (Arbitrary default)
water_temperature = 15.0  # [degrees Celsius] 'Temperature-report' gives 17 degrees surface temp in August and 'Temperature variation-report' gives variation of 2 degrees (highest temperature, so: August, is the worst case)
water_density = 1025.0  # [kg/m^3] Generic value
d50_soil = 0.0002  # [m]  Values given as 'range' in baggrund8 IEA report and confirmed by figure 2.2. in fish IEA report
d90_soil = 0.0005  # [m]  Values given as 'range' in baggrund8 IEA report and confirmed by figure 2.2. in fish IEA report
friction_angle = 35.0  # [degrees] Depth averaged friction angle from 'friction angle-report'
submerged_unit_weight = 10000.0  # [N/m^3] From 'friction angle-report', lighter layer ignored, because it is at great depth.
ref_storm_fraction = 0.6  # [-] (Storm fraction of time for Hs_ref) Slides of O&M lecture Gerard ('Accessibility of site (Vessel)') - Spare part optimisation report says vessels can sail out about 40% of the time
ref_storm_scale = 19.5  # [h] (Storm scale factor for Hs_ref - Lightning study ECN part 1 - IJmuiden minutiestortplaats) No data for Horns Rev found (not searched explicitly)
ref_storm_shape = 0.65  # [-] (Storm shape factor for Hs_ref - Lightning study ECN part 1 - IJmuiden minutiestortplaats) No data for Horns Rev found (not searched explicitly)
ref_hs_accessibility = 1.5  # [m] (Significant wave height for which the previous reference values apply) - Slides of O&M lecture Gerard ('Access systems considered')

# ------------------------------------------------------ Wind data - INPUT --------------------------------------------------------------------------------------
wind_direction_30 = ['N', 'NNE', 'ENE', 'E', 'ESE', 'SSE', 'S', 'SSW', 'WSW', 'W', 'WNW', 'NNW']
windrose_angle_3 = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75,
                    78, 81, 84, 87, 90, 93, 96, 99, 102, 105, 108, 111, 114, 117, 120, 123, 126, 129, 132, 135, 138,
                    141, 144, 147, 150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180, 183, 186, 189, 192, 195, 198,
                    201, 204, 207, 210, 213, 216, 219, 222, 225, 228, 231, 234, 237, 240, 243, 246, 249, 252, 255, 258,
                    261, 264, 267, 270, 273, 276, 279, 282, 285, 288, 291, 294, 297, 300, 303, 306, 309, 312, 315, 318,
                    321, 324, 327, 330, 333, 336, 339, 342, 345, 348, 351, 354, 357, 360]
windrose_angle_5 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115,
                    120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215,
                    220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315,
                    320, 325, 330, 335, 340, 345, 350, 355, 360]
windrose_angle_8 = [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176,
                    184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336,
                    344, 352, 360]
windrose_angle_10 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210,
                     220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 359]
windrose_angle_30 = [0.0, 30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0]
windrose_angle_360 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                      27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                      51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                      75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                      99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
                      119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137,
                      138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156,
                      157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175,
                      176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
                      195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213,
                      214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232,
                      233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251,
                      252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270,
                      271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289,
                      290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308,
                      309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327,
                      328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346,
                      347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]
mean_shape_fr = 2.33
mean_scale_fr = 10.71
# shape_fr = [2.08, 2.22, 2.41, 2.37, 2.51, 2.75, 2.61, 2.51, 2.33, 2.35, 2.58, 2.01] # It depends only on the wind direction
# scale_fr = [8.71, 9.36, 9.29, 10.27, 10.89, 10.49, 10.94, 11.23, 11.93, 11.94, 12.17, 10.31] # It depends only on the wind direction
wind_direction_prob_3 = [0.126666667, 0.380000001, 0.380000001, 0.380000001, 0.380000001, 0.380000001, 0.399999999,
                         0.399999999, 0.399999999, 0.399999999, 0.399999999, 0.399999999, 0.399999999, 0.399999999,
                         0.399999999, 0.399999999, 0.560000001, 0.560000001, 0.560000001, 0.560000001, 0.560000001,
                         0.560000001, 0.560000001, 0.560000001, 0.560000001, 0.560000001, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9,
                         0.9, 0.9, 0.9, 0.9, 0.909999999, 0.909999999, 0.909999999, 0.909999999, 0.909999999,
                         0.909999999, 0.909999999, 0.909999999, 0.909999999, 0.909999999, 0.63, 0.63, 0.63, 0.63, 0.63,
                         0.63, 0.63, 0.63, 0.63, 0.63, 0.620000001, 0.620000001, 0.620000001, 0.620000001, 0.620000001,
                         0.620000001, 0.620000001, 0.620000001, 0.620000001, 0.620000001, 0.96, 0.96, 0.96, 0.96, 0.96,
                         0.96, 0.96, 0.96, 0.96, 0.96, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.17, 1.23,
                         1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.23, 1.299999999, 1.299999999, 1.299999999,
                         1.299999999, 1.299999999, 1.299999999, 1.299999999, 1.299999999, 1.299999999, 1.299999999,
                         0.950000001, 0.950000001, 0.950000001, 0.950000001, 0.950000001, 0.950000001, 0.950000001,
                         0.950000001, 0.950000001, 0.950000001, 0.380000001, 0.380000001, 0.380000001, 0.380000001,
                         0.253333334]
wind_direction_prob_5 = [0.126666667, 0.633333335, 0.633333335, 0.633333335, 0.666666665, 0.666666665, 0.666666665,
                         0.666666665, 0.666666665, 0.666666665, 0.933333335, 0.933333335, 0.933333335, 0.933333335,
                         0.933333335, 0.933333335, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.516666665, 1.516666665, 1.516666665,
                         1.516666665, 1.516666665, 1.516666665, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.033333335,
                         1.033333335, 1.033333335, 1.033333335, 1.033333335, 1.033333335, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6,
                         1.95, 1.95, 1.95, 1.95, 1.95, 1.95, 2.05, 2.05, 2.05, 2.05, 2.05, 2.05, 2.166666665,
                         2.166666665, 2.166666665, 2.166666665, 2.166666665, 2.166666665, 1.583333335, 1.583333335,
                         1.583333335, 1.583333335, 1.583333335, 1.583333335, 0.633333335, 0.633333335, 0.506666668]
wind_direction_prob_8 = [0.126666667, 1.013333336, 1.020000002, 1.066666664, 1.066666664, 1.066666664, 1.226666666,
                         1.493333336, 1.493333336, 1.493333336, 2.060000001, 2.4, 2.4, 2.4, 2.423333331, 2.426666664,
                         2.426666664, 2.333333331, 1.68, 1.68, 1.68, 1.670000001, 1.653333336, 1.653333336, 1.653333336,
                         2.220000001, 2.56, 2.56, 2.56, 3.05, 3.12, 3.12, 3.14, 3.28, 3.28, 3.28, 3.349999999,
                         3.466666664, 3.466666664, 3.466666664, 2.883333334, 2.533333336, 2.533333336, 2.533333336,
                         1.203333336, 0.886666669]
wind_direction_prob_10 = [0.126666667, 1.26666667, 1.3, 1.33333333, 1.33333333, 1.6, 1.86666667, 1.86666667,
                          2.433333335, 3, 3, 3.009999999, 3.03333333, 3.03333333, 2.566666665, 2.1, 2.1, 2.083333335,
                          2.06666667, 2.06666667, 2.633333335, 3.2, 3.2, 3.55, 3.9, 3.9, 4, 4.1, 4.1, 4.216666665,
                          4.33333333, 4.33333333, 3.75, 3.16666667, 3.16666667, 2.21666667, 1.140000003]
wind_direction_prob_30 = [3.8, 4.3, 5.5, 8.3, 8.7, 6.7, 8.4, 10.5, 11.4, 12.2, 13.9,
                          6.1]  # The probabilty of the wind direction
wind_direction_prob_360 = [0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667,
                           0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667,
                           0.126666667, 0.126666667, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333,
                           0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333,
                           0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333,
                           0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.133333333,
                           0.133333333, 0.133333333, 0.133333333, 0.133333333, 0.186666667, 0.186666667, 0.186666667,
                           0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667,
                           0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667,
                           0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667,
                           0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.186666667, 0.3, 0.3, 0.3,
                           0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
                           0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.303333333, 0.303333333, 0.303333333,
                           0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333,
                           0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333,
                           0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333,
                           0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.303333333, 0.21, 0.21,
                           0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21,
                           0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.21, 0.206666667,
                           0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667,
                           0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667,
                           0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667,
                           0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667, 0.206666667,
                           0.206666667, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32,
                           0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32, 0.32,
                           0.32, 0.32, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39,
                           0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39, 0.39,
                           0.39, 0.39, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41,
                           0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41,
                           0.41, 0.41, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333,
                           0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333,
                           0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333,
                           0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333, 0.433333333,
                           0.433333333, 0.433333333, 0.433333333, 0.316666667, 0.316666667, 0.316666667, 0.316666667,
                           0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667,
                           0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667,
                           0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667,
                           0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.316666667, 0.126666667, 0.126666667,
                           0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667,
                           0.126666667, 0.126666667, 0.126666667, 0.126666667, 0.126666667]
# --------------------------------------------------- Power curve - INPUT ---------------------------------------------------------------------
wind_speed = [4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0,
              22.0, 23.0, 24.0, 25.0]  # wind speed in m/s
# electrical_power = [0.0,66.3,152.0,280.0,457.0,690.0,978.0,1296.0,1598.0,1818.0,1935.0,1980.0,1995.0,1999.0,2000.0,2000.0,2000.0,2000.0,2000.0,2000.0,2000.0,2000.0,2000.0,] #electrical power in KW

# powers = ['power7', 'power5', 'power3', 'powertable', 'powerstep']
powers = ['power7']

power_curve = ([[0.0, 0.0],
                [3.999, 0.0],
                [4.0, 66300.0],
                [5.0, 152000.0],
                [6.0, 280000.0],
                [7.0, 457000.0],
                [8.0, 690000.0],
                [9.0, 978000.0],
                [10.0, 1269000.0],
                [11.0, 1598000.0],
                [12.0, 1818000.0],
                [13.0, 1935000.0],
                [14.0, 1980000.0],
                [15.0, 1995000.0],
                [16.0, 1999000.0],
                [17.0, 2000000.0],
                [25.0, 2000000.0],
                [25.0001, 0.0],
                [1000.0, 0.0]])


# [Wind speed [m/s], Electrical power [W]]

# Power curve
def power7(U0):
    if U0 < 4.0:
        return 0.0
    elif U0 <= 25.0:
        return 3.234808e-4 * U0 ** 7.0 - 0.0331940121 * U0 ** 6.0 + 1.3883148012 * U0 ** 5.0 - 30.3162345004 * U0 ** 4.0 + 367.6835557011 * U0 ** 3.0 - 2441.6860655008 * U0 ** 2.0 + 8345.6777042343 * U0 - 11352.9366182805
    else:
        return 0.0


def power_table(U0):
    v = U0
    if v < 4: return 0.0
    if v == 4: return 66.3
    if v == 5: return 152.0
    if v == 6: return 280.0
    if v == 7: return 457.0
    if v == 8: return 690.0
    if v == 9: return 978.0
    if v == 10: return 1296.0
    if v == 11: return 1598.0
    if v == 12: return 1818.0
    if v == 13: return 1935.0
    if v == 14: return 1980.0
    if v == 15: return 1995.0
    if v == 16: return 1999.0
    if v == 17: return 2000.0
    if v == 18: return 2000.0
    if v == 19: return 2000.0
    if v == 20: return 2000.0
    if v == 21: return 2000.0
    if v == 22: return 2000.0
    if v == 23: return 2000.0
    if v == 24: return 2000.0
    if v == 25: return 2000.0


# ---------------------------------------------------- Thrust curve - INPUT -------------------------------------------------------------------------

# thrusts = ['Ct6', 'Ct4', 'Ct3', 'Cttable', 'Ctstep']
thrusts = ['Ct6']

thrust_curve = ([[0.0, 0.0],
                 [3.9999, 0.0],
                 [4.0, 0.1],
                 [5.0, 0.82],
                 [6.0, 0.8],
                 [7.0, 0.81],
                 [8.0, 0.81],
                 [9.0, 0.78],
                 [10.0, 0.74],
                 [11.0, 0.65],
                 [12.0, 0.57],
                 [13.0, 0.41],
                 [14.0, 0.31],
                 [15.0, 0.25],
                 [16.0, 0.2],
                 [17.0, 0.17],
                 [18.0, 0.14],
                 [19.0, 0.12],
                 [20.0, 0.1],
                 [21.0, 0.09],
                 [22.0, 0.08],
                 [23.0, 0.07],
                 [24.0, 0.06],
                 [25.0, 0.05],
                 [25.0001, 0.0],
                 [1000.0, 0.0]])


# [Wind speed [m/s], Thrust coefficient [-]]

# Thrust curve
def Ct_table(U0):
    v = U0
    if v < 4: return 0.1
    if v == 4: return 0.82
    if v == 5: return 0.81
    if v == 6: return 0.8
    if v == 7: return 0.81
    if v == 8: return 0.81
    if v == 9: return 0.78
    if v == 10: return 0.74
    if v == 11: return 0.65
    if v == 12: return 0.57
    if v == 13: return 0.41
    if v == 14: return 0.31
    if v == 15: return 0.25
    if v == 16: return 0.2
    if v == 17: return 0.17
    if v == 18: return 0.14
    if v == 19: return 0.12
    if v == 20: return 0.1
    if v == 21: return 0.09
    if v == 22: return 0.08
    if v == 23: return 0.07
    if v == 24: return 0.06
    if v == 25: return 0.05


def Ct6(U0):
    if U0 < 4.0:
        return 0.1
    elif U0 <= 25.0:
        return 7.3139922126945e-7 * U0 ** 6.0 - 6.68905596915255e-5 * U0 ** 5.0 + 2.3937885e-3 * U0 ** 4.0 + - 0.0420283143 * U0 ** 3.0 + 0.3716111285 * U0 ** 2.0 - 1.5686969749 * U0 + 3.2991094727
    else:
        return 0.1


# ---------------------------------------------------- Cable Cost - INPUTS --------------------------------------------------------------------------------------

V_rated_voltage = [22000, 33000, 45000, 66000, 132000, 220000]  # Rated voltage in V # User's option

P_rated = 3.6 * 10 ** 6  # W     # User's option

power_factor = 1.0  # cos angle
installation_cable_cost = 365  # Euros/meter
inflationrate = 1.18  # average inflation rate
exchangerate = 0.11  # exchange rate of SEK to Euros

# cost constants
Ap_init = [0.284, 0.411, 0.516, 0.688, 1.971, 3.181]  # must be multiplied by 10**6
Bp_init = [0.583, 0.596, 0.612, 0.625, 0.209, 0.11]  # must be multiplied by 10**6
Cp_init = [6.15, 4.1, 3.0, 2.05, 1.66, 1.16]  # must be multiplied by 10**6

# Cable procurement costs

cross_section = [95.0, 120.0, 150.0, 185.0, 240.0, 300.0, 400.0, 500.0, 630.0, 800.0, 1000.0]  # mm**2
current_rating = [300, 340, 375, 420, 480, 530, 590, 655, 715, 775, 825]  # Ampere
Cost = [206.0, 221.0, 236.0, 256.0, 287.0, 316.0, 356.0, 406.0, 459.0, 521.0, 579.0]  # Euros/meter
rv = 1  # User can pick each time one rated voltage. 0 represents the first place in a Python list
cr1 = 3  # User can pick two cable types, so he can select two values of rating current. 0 represents the first place in a Python list
cr2 = 7  # User can pick two cable types, so he can select two values of rating current. 0 represents the first place in a Python list

# -------------------------------------------------- Cable Topology - INPUT -----------------------------------------------------------------------
Crossing_penalty = 0
Area = []
# Transmission=[[central_platform_locations[0],[463000,5918000]],[central_platform_locations[1],[463000,5918000]]]
Transmission = []

# --------------------------------------------------- LPC/Costs - INPUT -----------------------------------------------------------------------------------------
i = 0.1  # interest rate [-]
v = 0.025  # inflation rate [-]
operational_lifetime = 20  # [years] - FIXED VALUE NOTE: The fixed price in PPA is valid for a number of full load hours that is reached in appr. 10 years. After that, market prices apply.
value_year = 2016
actual_year = 2016  # Year for which costs are expressed
management_percentage = 3.0  # [%]
distance_to_grid = 55000.0  # [m] Grid connection report: Submarine cable length 21 km - Onshore cable length 34 km - Total 50 km
distance_to_harbour = 20000.0  # [m] Spare part optimisation report says the 20 km sail to Horns Rev
onshore_transport_distance = 100000.0  # [m]
frequency = 50  # [Hz]
transmission_voltage = 220000.0  # [V]
grid_coupling_point_voltage = 169000.0  # [V]
rho_copper = 8940  # [kg/m^3]
rho_xlpe = 940  # [kg/m^3]
epsilon_0 = 8.85e-12  # [F/m]
epsilon_r = 2.3  # [-] (XLPE)


class cost1:
    def __init__(self, value, currency, year):
        global value_year
        # Inflation and exchange rate {'Currency Code': [Average inflation rate, Exchange rate to Euro]}
        self.conversion = {'USD': [2.57, 0.89],
                           'GBP': [2.55, 1.27],
                           'DKK': [1.84, 0.13],
                           'SEK': [2.03, 0.11],
                           'NOK': [1.95, 0.11],
                           'Euro': [2.16, 1.0]}

        inflation_rate = self.conversion[currency][0]
        exchange_rate = self.conversion[currency][1]

        self.ref_value = value
        self.currency = currency
        self.ref_year = year
        self.value = value * ((1.0 + (inflation_rate / 100.0)) ** (value_year - year)) * exchange_rate


# --------------------------------------------------Wind Farm - INPUT ----------------------------------------------------------

# Site Information/Inputs - Horns Rev
name = 'Cable topology of'
# WT_List=[[0,423974 ,6151447,0], [1,424033,6150889,0],[2,424092,6150332,0],[3,424151,6149774,0],[4,424210,6149216,0],[5,424268,6148658,0],[6,424327, 6148101,0],[7,424386,6147543,0],[8,424534,6151447,0],[9,424593,6150889,0],[10,424652,6150332,0],[11,424711,6149774,0],[12,424770,6149216,0],[13,424829,6148658,0],[14,424888,6148101,0],[15,424947,6147543,0],[16,425094,6151447,0],[17,425153,6150889,0],[18,425212,6150332,0],[19,425271,6149774,0],[20,425330,6149216,0],[21,425389,6148658,0],[22,425448,6148101,0],[23,425507,6147543,0],[24,425654,6151447,0],[25,425713,6150889,0],[26,425772,6150332,0],[27,425831,6149774,0],[28,425890,6149216,0],[29,425950,6148659,0],[30,426009,6148101,0],[31,426068,6147543,0],[32,426214,6151447,0],[33,426273,6150889,0],[34,426332,6150332,0],[35,426392,6149774,0],[36,426451,6149216,0],[37,426510,6148659,0],[38,426569,  6148101,0],[39,426628,  6147543,0],[40,426774,  6151447,0],[41,426833,  6150889,0],[42,426892,  6150332,0],[43,426952,  6149774,0],[44,427011,  6149216,0],[45,427070,  6148659,0],[46,427129,  6148101,0],[47,427189,  6147543,0],[48,427334,  6151447,0],[49,427393,  6150889,0],[50,427453,  6150332,0],[51,427512,  6149774,0],[52,427571,  6149216,0],[53,427631,  6148659,0],[54,427690,  6148101,0],[55,427749,  6147543,0],[56,427894,  6151447,0],[57,427953,  6150889,0],[58,428013,  6150332,0],[59,428072,  6149774,0],[60,428132,  6149216,0],[61,428191,  6148659,0],[62,428250,  6148101,0],[63,428310,  6147543,0],[64,428454,  6151447,0],[65,428513,  6150889,0],[66,428573,  6150332,0],[67,428632,  6149774,0],[68,428692,  6149216,0],[69,428751,  6148659,0],[70,428811,  6148101,0],[71,428870,  6147543,0],[72,429014,  6151447,0],[73,429074,  6150889,0],[74,429133,  6150332,0],[75,429193,  6149774,0],[76,429252,  6149216,0],[77,429312,  6148659,0],[78,429371,  6148101,0],[79,429431,  6147543,0]]
# WT_List=[[0,423974 ,6151447], [1,424033,6150889],[2,424092,6150332],[3,424151,6149774],[4,424210,6149216],[5,424268,6148658],[6,424327, 6148101],[7,424386,6147543],[8,424534,6151447],[9,424593,6150889],[10,424652,6150332],[11,424711,6149774],[12,424770,6149216],[13,424829,6148658],[14,424888,6148101],[15,424947,6147543],[16,425094,6151447],[17,425153,6150889],[18,425212,6150332],[19,425271,6149774],[20,425330,6149216],[21,425389,6148658],[22,425448,6148101],[23,425507,6147543],[24,425654,6151447],[25,425713,6150889],[26,425772,6150332],[27,425831,6149774],[28,425890,6149216],[29,425950,6148659],[30,426009,6148101],[31,426068,6147543],[32,426214,6151447],[33,426273,6150889],[34,426332,6150332],[35,426392,6149774],[36,426451,6149216],[37,426510,6148659],[38,426569,  6148101],[39,426628,  6147543],[40,426774,  6151447],[41,426833,  6150889],[42,426892,  6150332],[43,426952,  6149774],[44,427011,  6149216],[45,427070,  6148659],[46,427129,  6148101],[47,427189,  6147543],[48,427334,  6151447],[49,427393,  6150889],[50,427453,  6150332],[51,427512,  6149774],[52,427571,  6149216],[53,427631,  6148659],[54,427690,  6148101],[55,427749,  6147543],[56,427894,  6151447],[57,427953,  6150889],[58,428013,  6150332],[59,428072,  6149774],[60,428132,  6149216],[61,428191,  6148659],[62,428250,  6148101],[63,428310,  6147543],[64,428454,  6151447],[65,428513,  6150889],[66,428573,  6150332],[67,428632,  6149774],[68,428692,  6149216],[69,428751,  6148659],[70,428811,  6148101],[71,428870,  6147543],[72,429014,  6151447],[73,429074,  6150889],[74,429133,  6150332],[75,429193,  6149774],[76,429252,  6149216],[77,429312,  6148659],[78,429371,  6148101],[79,429431,  6147543]]

# WT_List = []


def myList(l):
    global WT_List
    WT_List = l

