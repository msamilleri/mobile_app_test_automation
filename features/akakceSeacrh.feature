Feature: Akakçe uygulamasında Laptop arama ve filtreleme

  Scenario: Kullanıcı laptop arar, filtreler ve ürün detayını kontrol eder
    Given Kullanıcı Akakçe uygulamasını açar
    When Üye olmadan devam et seçeneğine tıklar
    And Arama kutusuna "Laptop" yazar ve arar
    And Filtrele butonuna tıklar
    And Alt Kategori olarak "Bilgisayar,Donanım" seçer ve Ürünleri Gör butonuna tıklar
    And Sıralama seçeneklerinden "En Yüksek Fiyat" seçer
    And Sonuç ekranından 10. ürüne tıklar
    And Ürüne Git butonuna tıklar
    Then Ürün detay ekranında "Satıcıya Git" butonunun görüntülendiğini doğrular