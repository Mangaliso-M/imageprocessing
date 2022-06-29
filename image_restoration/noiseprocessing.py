#@Author Mangaliso M. Mngomezulu
#description: noise processing, creating noise and removing noise from images

from skimage.restoration import denoise_tv_chambolle, denoise_bilateral
from skimage.util import random_noise
from custom_lib import plot_comparison
from skimage import data

#load the image
image = data.astronaut()

#add noise to the image
noisy_image = random_noise(image)

#view the results 
plot_comparison(image, noisy_image, "Noisy Image")

#denoise the image; the higher the weight the more the noise, multichannel is for better color
denoised_image = denoise_tv_chambolle(noisy_image, weight=0.1, multichannel=True)

#denoised image
plot_comparison(noisy_image, denoised_image, "Denoised image")

#bilateral denoising, preserves the edges a lot more! much better
denoised_image = denoise_bilateral(noisy_image, multichannel=True)

plot_comparison(noisy_image, denoised_image, "Bilateral denoising")