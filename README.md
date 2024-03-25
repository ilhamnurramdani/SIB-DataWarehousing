# SIB-DataWarehousing
# Dokumentasi Class TargetedMarketingETL

Class ini adalah turunan dari class MarketingDataETL yang digunakan untuk melakukan ETL (Extract, Transform, Load) data pemasaran yang ditargetkan.

### Metode

1. **extract(self, df)**
   - Deskripsi: Metode ini digunakan untuk melakukan ekstraksi data dari file CSV.
   - Parameter:
     - `df`: String, nama file CSV yang berisi data pemasaran.
   - Output: DataFrame, data yang diekstraksi dari file CSV.

2. **transform(self)**
   - Deskripsi: Metode ini digunakan untuk melakukan transformasi data, termasuk pengubahan format tanggal dan pembersihan data.
   - Output: DataFrame, data yang telah ditransformasi.

3. **store(self)**
   - Deskripsi: Metode ini digunakan untuk menyimpan data yang telah ditransformasi ke dalam file CSV baru.
   - Output: Tidak ada.

4. **segment_customers(self)**
   - Deskripsi: Metode ini digunakan untuk mengelompokkan pelanggan berdasarkan kriteria tertentu, seperti pengeluaran total atau kategori produk yang dibeli.
   - Output: DataFrame, data pelanggan yang telah dikelompokkan.

### Contoh Penggunaan

```python
target_ETL = TargetedMarketingETL('marketing_data.csv')
target_ETL.Extract()
target_ETL.Transform()
result = target_ETL.Transform()
print("Data frame hasil pengelompokan:")
print(result)
