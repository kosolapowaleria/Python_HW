from address import Address
from mailing import Mailing

from_addr = Address(123456, 'Ленинград','Советская', '5','10')

to_addr = Address(654321, 'Холмск','Капитанская','8','10')

mailing = Mailing(to_address=to_addr, from_address=from_addr,cost=150,track='RU12356908')

print(mailing)