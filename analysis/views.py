import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive environments
import matplotlib.pyplot as plt
from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
import os

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file
            csv_file = request.FILES['file']
            data = pd.read_csv(csv_file)
            # Perform analysis
            head = data.head()
            description = data.describe()
            missing_values = data.isnull().sum()
            
            
            histograms = []
            for column in data.select_dtypes(include=['float64', 'int64']).columns:
                fig = data[column].hist().get_figure()
                fig.savefig(f'media/{column}_histogram.png')
                histograms.append(f'{column}_histogram.png')
                plt.close(fig)

            context = {
                'form': form,
                'head': head.to_html(),
                'description': description.to_html(),
                'missing_values': missing_values.to_frame(name='Missing Values').to_html(),
                'histograms': histograms,
            }
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
