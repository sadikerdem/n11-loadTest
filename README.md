# n11 Load Test (Locust)

Bu proje, **Locust** kullanılarak n11 ana sayfası üzerinde basit bir arama senaryosunun yük testi için hazırlanmıştır.  
Senaryo: **Anasayfaya gidilir → "iphone" araması yapılır**

---

## 🚀 Kullanılan Teknolojiler
- Python 3
- Locust (Load Testing Framework)

---

## 📁 Proje Yapısı
n11-loadtest/
│
├── locustfile.py
├── README.md
└── .gitignore

---

## 🔧 Kurulum

### Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

### Gerekli kütüphaneyi yükle
pip install locust

### Testi Çalıştır
locust

locuct arayüzü --> http://localhost:8089

---

## çıktılar
Toplam istek sayısı
	•	Ortalama yanıt süresi
	•	Percentile metrikleri
	•	Error rate
	•	Requests per second

Tüm sonuçlar Locust UI üzerinden canlı olarak görüntülenebilir.




