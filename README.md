# Anti Spam Filter for Pugaar

Spam Filter which removes spam, i.e., selectively passes complaints dedicated for VIT Men's Hostel.

## Usage :

```python3
>>> from pugaar_check import check
>>> check('broken door knob.')
True
>>> check('send me nudes xD')
False
>>> check(None)
True
```

## Tested and developed on :

  **Ubuntu 16.10 , Python 3.6.0 |Anaconda 4.3.1 (64-bit)**
