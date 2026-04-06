from ultralytics import YOLO

model = YOLO('yolov8n.pt')

images = [
    'https://upload.wikimedia.org/wikipedia/commons/e/ef/Freddie_Mercury_performing_in_New_Haven%2C_CT%2C_November_1977.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/b/b5/191125_Taylor_Swift_at_the_2019_American_Music_Awards_%28cropped%29.png',
    'https://upload.wikimedia.org/wikipedia/commons/9/99/Elvis_Presley_promoting_Jailhouse_Rock.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/1/17/Beyoncé_at_The_Lion_King_European_Premiere_2019.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/3/31/Michael_Jackson_in_1988.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/5/52/Adele_for_Vogue_in_2021.png',
    'https://upload.wikimedia.org/wikipedia/commons/e/e1/David-Bowie_Chicago_2002-08-08_photograph_by_Adam_Bielawski.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/c/c2/Rihanna_at_the_Diamond_Ball_2017.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/c/c1/Ed_Sheeran-6886.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/d/d4/Lady_Gaga_at_the_TIFF_in_2017.jpg'
]