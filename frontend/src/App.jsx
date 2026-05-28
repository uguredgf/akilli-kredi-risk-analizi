import React, { useState } from 'react';
import './App.css'; // Kendi CSS/Bootstrap tasarımlarını buraya ekleyebilirsin

function App() {
  const API_CANDIDATES = [
    'http://localhost:5000/tahmin',
    'http://localhost:5001/tahmin'
  ];

  // Kullanıcı girdilerini tutacağımız state'ler
  const [formData, setFormData] = useState({
    gelir: '',
    borc: '',
    kredi_gecmisi: 1, // Kredi geçmişi genelde 0 veya 1 olur
    yas: ''
  });

  // Tahmin sonucunu ve olası hataları tutacağımız state'ler
  const [sonuc, setSonuc] = useState(null);
  const [hata, setHata] = useState(null);
  const [yukleniyor, setYukleniyor] = useState(false);

  // Form elemanları değiştikçe state'i güncelleyen fonksiyon
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // Form gönderildiğinde Flask API'ye istek atan fonksiyon
  const handleSubmit = async (e) => {
    e.preventDefault();
    setHata(null);
    setSonuc(null);
    setYukleniyor(true);

    try {
      const payload = {
        gelir: Number(formData.gelir),
        borc: Number(formData.borc),
        kredi_gecmisi: Number(formData.kredi_gecmisi),
        yas: Number(formData.yas)
      };

      if (payload.gelir <= 0 || payload.borc < 0 || payload.yas <= 0) {
        throw new Error('Gelir ve yaş pozitif olmalı, borç negatif olamaz.');
      }

      let sonHata = null;

      for (const apiUrl of API_CANDIDATES) {
        try {
          const response = await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });

          const data = await response.json().catch(() => ({}));

          if (!response.ok) {
            throw new Error(data.error || data.details || 'Sunucu hatası oluştu.');
          }

          const normalizeSonuc = data.sonuc || data.kredi_durumu;
          if (!normalizeSonuc) {
            throw new Error('API yanıtında sonuç alanı bulunamadı.');
          }

          setSonuc(normalizeSonuc);
          sonHata = null;
          break;
        } catch (error) {
          sonHata = error;
        }
      }

      if (sonHata) {
        throw sonHata;
      }

    } catch (error) {
      setHata(error.message);
    } finally {
      setYukleniyor(false);
    }
  };

  return (
    <div className="page">
      <div className="container">
        <h1>Akıllı Kredi Risk Analizi</h1>
        <p className="subtitle">
          Gelir, borç, kredi geçmişi ve yaş bilgisine göre kredi risk tahmini üretir.
        </p>

        <form onSubmit={handleSubmit} className="form-container">
          <div>
            <label>Gelir (TL)</label>
            <input type="number" min="1" name="gelir" value={formData.gelir} onChange={handleChange} required />
          </div>

          <div>
            <label>Borç (TL)</label>
            <input type="number" min="0" name="borc" value={formData.borc} onChange={handleChange} required />
          </div>

          <div>
            <label>Kredi Geçmişi</label>
            <select name="kredi_gecmisi" value={formData.kredi_gecmisi} onChange={handleChange}>
              <option value={1}>İyi (1)</option>
              <option value={0}>Kötü (0)</option>
            </select>
          </div>

          <div>
            <label>Yaş</label>
            <input type="number" min="18" max="100" name="yas" value={formData.yas} onChange={handleChange} required />
          </div>

          <button type="submit" disabled={yukleniyor}>
            {yukleniyor ? 'Hesaplanıyor...' : 'Risk Analizi Yap'}
          </button>
        </form>

        {/* API'den sonuç dönerse ekranda göster */}
        {sonuc && (
          <div className={`sonuc ${sonuc === 'riskli' ? 'riskli' : 'risksiz'}`}>
            <h2>
              {sonuc === 'riskli' ? 'KREDI REDDEDILDI (RISKLI)' : 'KREDI ONAYLANDI (RISKSIZ)'}
            </h2>
          </div>
        )}

        {/* Hata olursa ekranda göster */}
        {hata && (
          <div className="hata">
            <p>{hata}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;