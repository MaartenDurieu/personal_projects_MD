from sequence_solver import NumberSeriesPredictor

if __name__ == '__main__':
    predictor = NumberSeriesPredictor()
    predictor.derive_formula('1234,56789')
    # predictor.predict_next_number()