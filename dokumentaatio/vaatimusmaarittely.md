# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on hirsipuu-peli. Pelissä on yksi pelaaja, joka pyrkii arvaamaan annetun sanan syöttämällä kirjaimia yksi kerrallaan. 


## Toiminnallisuus

### Aloitus

Pelaaja aloittaa pelin. Peli generoi jonkin sanan, jonka pituus näkyy näytöllä viivoina. Pelissä on 50 sanamahdollisuutta, jotka on valmiiksi syötetty peliin. 

### Pelaaminen
Pelaaja syöttää jonkin kirjaimen. Jos kirjain on sanassa, tulee kaikki kyseiset kirjaimet näkyviin. Jos kirjain ei ole sanassa, hirttomies-kuvaan tulee yksi elementti lisää.
Samaa kirjainta ei voi syöttää enempää kuin yhden kerran. Hirttomies kuvassa on kuusi elementtiä. 

### Pelin päättyminen
Jos pelaaja saa koko sanan arvattua ennen kuin hirttomies-kuva on valmis, pelaaja voittaa. Jos hirttomies on valmis ennen kuin sana on kokonaan arvattu, pelaaja häviää. 
Pelaajalla saa siis mennä kuusi kirjainta väärin, ennen kuin pelaaja häviää. 

## Käyttöliittymäluonnos
Peli aukeaa omassa ikkunassa. Peli koostuu kolmesta eri näkymästä. 

### Aloitusnäkymä
Tähän näkymään peli aukeaa. Siinä pelaaja voi klikata "Aloita peli"

### Pelinäkymä
Pelinäkymässä pelataan itse peli. Tässä näkymässä on hirttomies-kuva, kirjaimet ja sanan pituus viivoina. 

### Lopetusnäkymä
Tähän näkymään päädytään kun peli on voitettu tai hävitty. Tästä näkymästä pelin voi pelata uudelleen tai lopettaa pelaamisen. 


## Jatkokehitysideoita
- Peliä voisi laajentaa niin, että pelaajalla on aikaraja. 
- Pelissä voisi olla mahdollisuus itse lisätä sanoja peliin. 
- Pelissä voisi olla mahdollisuus valita solo-pelin lisäksi duo-peli, jossa vuorotellen pelaajat valitsisivat toiselle pelaajalle sanan jota arvata. 
- Peliin voitaisiin myös lisätä hallinnoiva käyttäjä, joka voisi esimerkiksi muokata pelin sanavaihtoehtoja. 


