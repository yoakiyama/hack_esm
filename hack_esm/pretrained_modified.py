import .pretrained 

def load_esm_state_dict(esm_model):
    model_data, regression_data = pretrained._download_model_and_regression_data(model_name)