## Ohjelmistotekniikka, harjoitustyö

# Blackjack
Sovelluksessa käyttäjä voi pelata blackjack-korttipeliä jakajaa vastaan. 

## Dokumentaatio

[Alustava vaatimusmäärittely](https://github.com/n1k1k/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/n1k1k/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/n1k1k/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus
Riippuvuudet asennetaan komennolla
```bash
poetry install
```

Tämän jälkeen sovellus voidaan käynnistää komennolla
```bash
poetry run invoke start
```

## Komentorivitoiminnot

Sovelluksen suorittaminen onnistuu asennuksen jälkeen komennolla
```bash
poetry run invoke start
```

Testaus suoritetaan komennolla
```bash
poetry run invoke tests
```

Testikattavuusraportti suoritetaan komennolla 
```bash
poetry run invoke coverage-report
```

Pylint tarkistukset suoritetaan komennolla 
```bash
poetry run invoke lint
```
