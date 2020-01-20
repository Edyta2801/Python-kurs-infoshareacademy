try:
    print('To jest blok try')
    raise ValueError('Wywolany wyjatek')
except Exception as e:
    print('zlapalem wyjatek: ', e)
finally:
    print('To jest blok finally, tutaj kod zawsze jest wywołany')
