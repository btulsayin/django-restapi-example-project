
# REST APİ NEDİR? 

Günümüzde iki sistemin haberleşmesinde kullanılan popüler olmuş iki tip servis haberleşmesi vardır.SOAP ve REST

- REST client-server iletişimiyle ilgili bir mimaridir. 
- SOAP gibi kompleks mimarilerle uğraşmak yerine, HTTP protokolü üzerinden veri geçişini sağlamaktadır.
- Esnek olup, SOAP gibi keskin standartları ve kuralları yoktur.
- SOAP ile en büyük farkı bizi proxy kullanmaya, bir WSDL’e  zorlamıyor olması ve kolay entegre olmasıdır.

** REST Request Tipleri **

- GET :  Belirtilen collection’ın (toplanacak verinin) URL’lerini veya detaylarını listelemede kullanılır.
- PUT : Bütün bir collection’ın bir başka collection ile yer değiştirmek için kullanılır. 
       Örnek: Twitter api’de kullanıcının paylaştığı gönderiyi düzenlemek olabilir.
- POST : Yeni bir collection oluşturmak için kullanılır ve yeni oluşturan collection’ın URI’si döndürülür. 
        Örnek : Twitter api’de yeni gönderi paylaşma olabilir.
- DELETE : Belirtilen Collection’ı silmek için kullanılır. Örneğin Twitter api kullanarak bir gönderiyi silmek.
