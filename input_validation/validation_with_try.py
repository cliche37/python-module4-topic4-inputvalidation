def average(score1, score2, score3):

    try:
        if score1 or score2 or score3 < 0:
            raise Exception('Negative numbers are not accepted. Please alter input.')
    except Exception as error:
        raise ValueError
        print('Negative numbers are not accepted. Please alter input.')

    number_of_tests = 3
    return float((score1 + score2 + score3) / number_of_tests)
