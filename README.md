# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi. Untuk step by step guide, Bapak Ibu dipersilahkan untuk membuka git saya [Click here](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Webscrapping with Beautiful Soup"). Kita juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi kita.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Atau Bapak Ibu cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (6 points)
- Creating data frame & Data wrangling (6 points)
- Implement it on flask dashboard (2 points)


## What You Need to Do

* Silahkan mencoba melakukan scraping soal di bawah menggunakan `beautiful soup` di notebook Bapak/Ibu terlebih dahulu.
* Bapak/Ibu dapat men-clone repo ini.
* File di repo ini adalah skeleton yang dapat digunakan untuk membuat flask dashboard sederhana.
* Silahkan isi di bagian yang masih kosong.
* Isi fungsi `scrap` dengan proses scraping yang sudah Bapak/Ibu lakukan di notebook. 

```python
table = soup.find(___)
tr = table.find_all(___)
```

* Isi bagian ini untuk menyimpan hasil scrap yang Bapak/Ibu buat menjadi sebuah dataframe.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Terakhir Bapak/Ibu dapat menggunakan fungsi `scrap` dengan cara mengisi bagian berikut dengan link web yang Bapak/Ibu scrap.

```python
df = scrap(___) #insert url here
```

* Bapak/Ibu juga dapat bermain dengan UI nya pada `index.html` yang dimana Bapak/Ibu dapat mengikuti comment yang ada untuk mengetahui bagian mana yang dapat diubah. 

### The Final Mission

Pada captsone kali ini, Bapak Ibu bisa memilih salah satu soal ini untuk dikerjakan.

1. Data kurs Japan Yen ke rupiah pada tahun 2019 dari `monexnews.com/kurs-valuta-asing.htm?kurs=JPY`

    * Dari halaman tersebut carilah `kurs jual`, `Kurs beli` dan `tanggal`
    * Bualah plot pergerakan kurs JPY pada tahun 2019

2. Data film yang rilis di tahun 2019 dari `imdb.com/search/title/?release_date=2019-01-01,2019-12-31`

    * Dari Halaman tersebut carilah `judul` , `imdb rating` , `metascore`, dan `votes`
    * Buatlah plot dari 7 film paling populer di tahun 2019.


Happy learning~
