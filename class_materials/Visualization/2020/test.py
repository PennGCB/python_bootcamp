import statistics

import scipy.stats


def test_mean(data, prediction):
    try:
        assert abs(statistics.mean(data) - prediction) < .01
    except AssertionError:
        print('Your calculate_mean function is not working correctly')
        return
    except TypeError:
        print('Your calculate_mean function has not been implemented yet')
        return
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
        return
    except TypeError:
        print('Your calculate_regression_coeff function has not been implemented yet')
        return
    print('Your calculate_regression_coeff function is correct')

def test_heatmap_read(df):
    '''Test that the student read in the dataframe correctly'''
    try:
        assert len(df) == 30
    except AssertionError:
        print("Your dataframe isn't the correct length. Are you sure you read the right file?")
        return
    except TypeError:
        print('Your create_dataframe function has not been implemented yet')
        return
    try:
        assert len(df.columns) == 6
    except AssertionError:
        print("Your dataframe doesn't have the correct number of columns, are you sure you read the right file?")
        return

    print('You successfully read in your dataframe')

def test_heatmap_melt(df):
    '''Test that the heatmap dataframe was melted correctly'''
    try:
        assert len(df.columns) == 3
    except AssertionError:
        print("Your dataframe doesn't have the correct number of columns.")
        print("The dataframe should have a column for genes, case/control status, and expression")
        print("Printing the first few rows of your dataframe with df.head() might help find the bug")
        return
    except AttributeError:
        print('Your melt_dataframe function has not been implemented yet')
        return

    try:
        assert len(df) == 150
    except AssertionError:
        print("Your dataframe doessn't have the correct number of rows.")
        print("The dataframe should have a column for genes, case/control status, and expression")
        print("Printing the first few rows of your dataframe with df.head() might help find the bug")
        return

    print('You successfully reformated your dataframe')


