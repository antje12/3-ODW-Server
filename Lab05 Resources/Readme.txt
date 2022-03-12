Information vedrørende Lab 05
Til denne lab skal der arbejdes med Kubernetes :slight_smile: 
Her skal en controller installeres på jeres maskiner, der gør det muligt at kommunikere og kontrollere et cluster vi har hostet på SDU.
Alt dette er der forklaret mere om i Lab 05.

For at forbinde til vores cluster, er der behov for en config (til hverdag kaldt kubeconfig), som indeholder oplysninger om hvilket cluster der skal forbindes til og hvem der forbinder.
Filen odw-config.enc er en krypteret config-fil som kan benyttes, men den skal selvfølgelig dekrypteres før brug :slight_smile: 

For at dekryptere filen skal følgende command bruges $ openssl aes-256-cbc -d -a -salt -in [ENCRYPTED-FILENAME] -out [DECRYPTED-FILENAME]
Standarden er, at man kalder sin kubeconfig for config. Har man dog allerede en kubeconfig der hedder det (hint til alle SE :sweat_smile:), kan man kalde den noget andet.
Standarden er ligeledes at man under sit home, altså /home/[USER] laver en mappe der hedder .kube, hvor config-filen gemmes.

Når man dekrypterer filen efterspørges der et password. Det er y7xSuG6MbEjUnA.


Men alt skal selvfølgelig ikke være så nemt. Nogle OS' f.eks. MacOS kører en anden version af openssl som kan give fejl.
Er det tilfældet, kan i lave en interaktiv container der kører ubuntu, hvor i mounter et volume.
Det betyder, at man "binder" en mappe fra sin host-maskine til containeren. På den måde vil indholdet af mappen være tilgængelig i containeren og de ændringer der laves (på enten host eller container) vil gælde begge steder.
docker run --rm -i -t -v [PATH-TO-FOLDER-ON-HOST]:[PATH-TO-FOLDER-IN-CONTAINER] ubuntu bash

Derefter skal openssl hentes også kan man bruge ovennævnte command ($ openssl aes-256-cbc -d -a -salt -in [ENCRYPTED-FILENAME] -out [DECRYPTED-FILENAME]) til at dekryptere filen.
