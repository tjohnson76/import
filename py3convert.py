import codecs
import pymarc


input = 'records_in.mrc'
output = 'records_out.xml'

reader = pymarc.MARCReader(open(input, 'rb'), to_unicode=True)
writer = codecs.open(output, 'w', 'utf-8')
for record in reader:
    record.leader = record.leader[:9] + 'a' + record.leader[10:]
    writer.write(bytes.decode(pymarc.record_to_xml(record)) + '\n')
