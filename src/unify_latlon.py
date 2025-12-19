def unify_latlon(ds):
    """把经纬度维度统一成 lat / lon，其他维度保持不变。"""
    rename_dict = {}
    if 'latitude' in ds.dims:
        rename_dict['latitude'] = 'lat'
    if 'Latitude' in ds.dims:
        rename_dict['Latitude'] = 'lat'
    if 'longitude' in ds.dims:
        rename_dict['longitude'] = 'lon'
    if 'Longitude' in ds.dims:
        rename_dict['Longitude'] = 'lon'
    if rename_dict:
        ds = ds.rename(rename_dict)
    return ds

import matplotlib.pyplot as plt

def plot_history(train_losses, val_losses):
    """
    绘制训练集和验证集 loss 曲线
    """
    plt.figure(figsize=(8, 5))
    plt.plot(train_losses, label='Train Loss')
    plt.plot(val_losses, label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss (MSE)')
    plt.title('Training History')
    plt.legend()
    plt.grid(True)
    plt.show()
