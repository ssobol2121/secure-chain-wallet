# Dust Detector

**Dust Detector** — инструмент для выявления пылевых UTXO на Bitcoin-адресе.

## Что делает

- Сканирует адрес на наличие мелких (dust) выходов
- Отображает хеш транзакции, индекс и сумму
- Помогает в оценке загрязнённости кошелька пылью

## Порог

По умолчанию `dust_threshold = 546 сатоши`, как в Bitcoin Core.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python dust_detector.py <bitcoin_address>
```

## Пример

```bash
python dust_detector.py 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
```

## Применение

- Очистка кошельков от пыли
- Forensics-анализ
- Выявление подозрительных микропереводов

## Лицензия

MIT License
