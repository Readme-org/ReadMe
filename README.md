# Kelompok Project

### Anggota Kelompok :

1. Winoto Hasyim - 2206025243
2. Ghany Rasyid Prawira - 2206082392
3. Galen Taris Bariqi - 2206029052
4. Rizqi Bayu Utama - 2206826330
5. Jessica Ruth Damai Yanti Manurung - 2206082783

## Deskripsi Website dan Manfaat

**ReadMe** adalah sebuah aplikasi web yang menggunakan kecerdasan buatan untuk merekomendasikan buku kepada penggunanya berdasarkan masalah atau topik yang mereka hadapi. Website ini menggunakan AI yang memungkinkan pengguna untuk mendapatkan rekomendasi buku dengan menyampaikan apa yang mereka butuhkan, misalnya "saya ingin belajar python dari awal". Website ini nantinya akan memberikan rekomendasi buku dengan detail lengkap seperti deskripsi, ulasan, serta rating dari pengguna lain. Selain dari masalah yang digambarkan, aplikasi akan mempertimbangkan riwayat baca pengguna, ulasan yang mereka berikan, dan buku yang ditandai sebagai favorit. 

### Manfaat dari Website Ini

- **Mempermudah pencarian rekomendasi buku :** Pengguna mendapatkan rekomendasi buku yang sesuai dengan minat mereka sehingga mereka lebih mungkin menemukan buku-buku yang mereka nikmati.
- **Memberikan referensi yang lebih variatif :** Masyarakat mendapatkan akses ke berbagai genre dan topik buku sehingga mereka dapat meningkatkan pengetahuan mereka dalam berbagai bidang.
- **Meningkatkan efisiensi waktu :** Website ini dapat mempermudah pengguna dalam mendapatkan informasi relevan terkait buku yang dicari sehingga dapat meningkatkan efisiensi waktu.
- **Meningkatkan Literasi masyarakat :** Membantu meningkatkan minat membaca di kalangan masyarakat dengan memberikan akses mudah ke berbagai buku, termasuk yang berkualitas.

## Daftar Modul

1. Home Page (Ghany)
Halaman awal ReadMe dirancang sebagai tampilan utama yang intuitif memastikan pengguna dapat dengan cepat memahami cara kerja aplikasi tanpa perlu banyak eksplorasi. Page ini menggunakan elemen visual yang menarik dengan beberapa ilustrasi bernuansa modern simple untuk menciptakan kesan mendalam. Selain itu, page ini menampilkan logo, nama aplikasi, dan slogan atau deskripsi singkat tentang apa yang dilakukan oleh aplikasi.
2. Autentikasi (Jessica)
Dengan fitur autentikasi, pengguna dapat membuat akun pribadi mereka, memastikan bahwa tidak ada akses yang tidak sah ke data pribadi pengguna. Fitur autentikasi ini memuat Register page dan Login page sebelum pengguna akan diarahkan ke main page. Terakhir, pada autentikasi juga akan ditambahkan fitur lupa kata sandi yang membantu pengguna untuk recovery akun mereka apabila lupa username/password.
3. Search Module (Ghany)
Inti dari aplikasi, di mana AI akan bekerja untuk memberikan rekomendasi buku.  Fitur ini terdapat pada home page yang dimana website akan meminta user untuk memasukkan permintaan mereka, kemudian AI akan memproses dan  merekomendasikan buku yang paling relevan.
4. List Book Page (Galen)
Halaman yang menampilkan daftar buku dari dataset aplikasi dan akan ada tombol untuk mengarahkan ke fitur ini ada pada search modul. List book page berguna untuk memudahkan pengguna melihat daftar buku yang ada pada dataset sehingga bisa mencari beberapa referensi lain. 
5. Book Details Page (Bayu)
Halaman khusus untuk setiap buku yang menampilkan informasi lengkap seperti sinopsis, rangkuman, pengarang, dan ulasan pengguna. Book details page ini berguna untuk membuat pengguna mengetahui isi buku secara kasar tanpa harus membaca seluruh isi bukunya.
6. Rating & Ulasan Buku (Galen)
Fitur interaktif yang memungkinkan pengguna dapat memberikan umpan balik serta berbagi pendapat tentang buku tertentu. Dengan fitur ini, pengguna dapat memberikan ulasan dan rating buku yang direkomendasikan untuk membantu pengguna lain yang mencari rekomendasi buku tersebut. Rating dan ulasan buku ini akan ditampilkan pada halaman book details page.
7. Sorting Buku (At o)
Mekanisme yang memberi pengguna kontrol untuk menampilkan buku dalam urutan atau kategori tertentu.  Alat ini memungkinkan pengguna untuk mengkombinasikan beberapa kriteria sorting, seperti abjad dan rating.
8. Read List (Wishlist) (Bayu)
Sebuah daftar khusus di mana pengguna dapat menyimpan buku yang mereka temukan menarik dan ingin baca di kemudian hari. Pengguna juga dapat menambahkan atau menghapus buku dari Read List tersebut. 

## Role User

1. **Guest** 
Guest adalah mereka yang mengakses aplikasi ReadMe tanpa perlu masuk atau mendaftar. Mereka hanya dapat melihat List Book Page, mencari buku dalam dataset, melihat detail buku, dan mengeksplorasi fitur dasar aplikasi, tetapi tidak bisa melihat ulasan, memberikan ulasan, dan beberapa fitur lainnya.

2. **Registered User**
Registered user adalah mereka yang telah membuat akun di aplikasi ReadMe. Mereka memiliki hak akses lebih terhadap fitur-fitur yang dimiliki oleh aplikasi ReadMe dibandingkan guest user dan dapat berkontribusi aktif untuk memberikan ulasan serta ranking suatu buku.

## Sumber Dataset Katalog Buku

Untuk sumber data katalog buku, kami menggunakan Google Books API untuk mengambil informasi buku terkait judul, penulis, deskripsi, serta sampul buku tersebut. 