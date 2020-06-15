import statistics

import scipy.stats


def test_mean(data, prediction):
    try:
        assert abs(statistics.mean(data) - prediction) < .01
    except AssertionError:
        print('Your calculate_mean function is not working correctly')
    except TypeError:
        print('Your calculate_mean function has not been implemented yet')
    print('Your calculate_mean function is correct')

def test_regression(x, y, prediction_slope, prediction_intercept):
    regression = scipy.stats.linregress(x, y)
    intercept = regression.intercept
    slope = regression.slope

    try:
        assert abs(prediction_intercept - intercept) < .01
        assert abs(prediction_slope - slope) < .01
    except AssertionError:
        print('Your calculate_regression_coeff function is not working correctly')
    except TypeError:
        print('Your calculate_regression_coeff function has not been implemented yet')
    print('Your calculate_regression_coeff function is correct')
