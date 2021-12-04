# OTP

Just for Fun, simple Umsetzung des OTPs. Später soll noch eine GUI hinzukommen. 

! Keyerzeugung erfolgt mit Pythons internen Zufallszahlengenerator, der ist berechenbar und nicht kryptographisch sicher! 

Der zu verschlüsselnde Text wird in einer Datei mit der Bezeichnung "Klartext.txt" gespeichert
Dieser muss im selben Ordner wie die 3 Pythonprogramme liegen.

keyerzeugen.py erzeugt eine Datei "key.txt" in dem der gernerierte Schlüssel abgelegt wird.
chiffrieren.py erzeugt mit den generierten Key aus der key.txt ein Chiffrat und legt es in der Datei "chiffrratt.txt" ab.
chiffrierenUNDkeyerzeugen.py erlegt beides in einen Zug.
"dechiffrieren.py" dechiffriert mittels des Keys in der key.txt Datei, das Chiffrat und erzeugt die Datei "Klartext.txt" und legt den Klartext darin ab.
