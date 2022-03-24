from imapy_music import IMA

if __name__ == '__main__':
    onsets = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 14, 16, 17, 18, 20, 21, 22, 24, 25, 26, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 44, 46, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58]

    ima_calculator = IMA(onsets=onsets)

    # Recalculate Weights with different parameters:
    # ima_calculator.calculateWeights(onsets, 3, 2, 1, 2, 1)

    print(ima_calculator.calculate_IMA_score())