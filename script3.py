using
System;
using
System.IO;

namespace
LoggingExample
{
// Logija
liides(tavaliselt
defineeritakse
eraldi
failis)
public
interface
ILogger
{
    void
Info(string
message);
void
Error(string
message);
}

// FileLogger
klass
realiseerib
ILogger
liidese
ja
IDisposable(ressursside
korrektseks
vabastamiseks)
public


class FileLogger: ILogger, IDisposable


{
    private
readonly
FileStream
_fileStream; // Faili
madala
taseme
voog
private
readonly
StreamWriter
_streamWriter; // Teksti
kirjutamiseks
mugav
klass

// Konstruktor – võtab
vastu
failinime
public
FileLogger(string
fileName)
{
// Avame
faili
kirjutamiseks(kui
pole
olemas, loome
uue), lisame
lõppu
_fileStream = new
FileStream(fileName, FileMode.OpenOrCreate, FileAccess.Write, FileShare.Read);

// Liigume
faili
lõppu, et
vanu
logisid
ei
kirjutataks
üle
_fileStream.Seek(0, SeekOrigin.End);

// Loome
StreamWriter
'i teksti kirjutamiseks
_streamWriter = new
StreamWriter(_fileStream);
}

// Info - tüüpi
logi
kirjutamine
public
void
Info(string
message)
{
    Write("INFO: " + message);
}

// Veateate
logi
kirjutamine
public
void
Error(string
message)
{
    Write("ERROR: " + message);
}

// Privaatne
meetod – tegelik
kirjutamine
faili
private
void
Write(string
message)
{
    _streamWriter.WriteLine(message);
// Võid
lisada
_streamWriter.Flush();
kui
tahad, et
logid
kohe
faili
jõuaksid
}

// IDisposable
realiseerimine – kohustuslik
ressursside
vabastamiseks
public
void
Dispose()
{
// Sunnime
kõik
puhvris
olevad
andmed
faili
kirjutama
_streamWriter.Flush();

// Sulgeme
kirjutaja
ja
failivoo
_streamWriter.Dispose();
_fileStream.Dispose();
}
}

// Näide
kasutamiseks(testiks)


class Program
    {
        static
    void
    Main(string[]
    args)
    {
    // Soovitatav
    kasutada
    using - blokki – Dispose
    kutsutakse
    automaatselt
    using(var
    logger = new
    FileLogger("app.log"))
    {
        logger.Info("Rakendus käivitati edukalt");
    logger.Info("Toimub mingi operatsioon...");
    logger.Error("Oi, tekkis viga!");
    logger.Info("Kõik parandatud, jätkame tööd");
    } // ← Siin
    kutsutakse
    automaatselt
    Dispose()

    Console.WriteLine("Logid on kirjutatud faili app.log");
    Console.ReadKey();
    }
    }
    }