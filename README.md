# 🏃‍♂️ Soļu Skaitītāja Programma

## 📋 Apraksts

Šī ir vienkārša Python programma, kas ļauj lietotājiem:

- Reģistrēties un ielogoties ar savu lietotājvārdu un paroli
- Ievadīt ikdienas soļu skaitu katrai nedēļas dienai
- Apskatīt rezultātus un vidējo soļu skaitu
- Saglabāt datus failā `step_data.txt`

Programma sastāv no vairākām daļām, kas sadalītas pa moduļiem, lai nodrošinātu labāku strukturējumu un uzturēšanu.

---

## 📁 Failu struktūra

```
projekts/
│
├── main.py              # Galvenā programma
├── login.py             # Reģistrācijas un ielogošanās funkcionalitāte
├── step_data.py         # Soļu ievade un rezultātu parādīšana
├── menu.py              # Lietotāja izvēlnes parādīšana
├── ascii.py             # ASCII māksla programmai
├── step_data.txt        # Saglabātie dati par soļiem
└── README.md            # Šis apraksts
```

---

## 🔧 Kā lietot

1. **Palaidiet programmu** ar komandu:
   ```bash
   python main.py
   ```

2. **Piesakieties vai reģistrējieties** ar savu lietotājvārdu.

3. **Izvēlnē izvēlieties darbību**:
   - `1` — ievadīt soļu skaitu
   - `2` — apskatīt rezultātus
   - `3` — iziet no programmas

---

## 📝 Datu ievade un glabāšana

- Dati tiek ievadīti lietotāja veidā pa katrai nedēļas dienai.
- Visi dati tiek saglabāti failā `step_data.txt`, kur redzams katras dienas soļu skaits.

---

## 💡 Nākotnes uzlabojumi

- Paroļu šifrēšana drošībai
- Datu saglabāšana katram lietotājam atsevišķi
- Grafiska lietotāja saskarne (GUI)
- Soļu dati vairākām nedēļām
- Statistika ar grafikām

---

## 📌 Prasības

- Python 3.x
- Nav nepieciešamas papildu bibliotēkas (tiek izmantotas tikai standarta Python funkcijas)

---

## 🌐 Valoda

Visa programma un tās izvade ir latviešu valodā.
