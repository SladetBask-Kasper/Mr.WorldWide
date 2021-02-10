data1 = "k-	kh-	g-	gh-	ṅ-	c-	ch-	j-	jh-	ñ-	ṭ-	ṭh-	ḍ-	ḍh-	ṇ-	t-	th-	d-	dh-	n-	p-	ph-	b-	bh-	m-	y-	r-	l-	v-	ś-	ṣ-	s-	h-"
data2 = "𑀓	𑀔	𑀕	𑀖	𑀗	𑀘	𑀙	𑀚	𑀛	𑀜	𑀝	𑀞	𑀟	𑀠	𑀡	𑀢	𑀣	𑀤	𑀥	𑀦	𑀧	𑀨	𑀩	𑀪	𑀫	𑀬	𑀭	𑀮	𑀯	𑀰	𑀱	𑀲	𑀳"
data3 = "क	ख	ग	घ	ङ	च	छ	ज	झ	ञ	ट	ठ	ड	ढ	ण	त	थ	द	ध	न	प	फ	ब	भ	म	य	र	ल	व	श	ष	स	ह"

def printArray(a, arrayName = "x"):
	print(f"{arrayName} = [", end="")
	output = ""
	for i in a:
		output += f'"{i}", '
	output = output[:-2] + "]"
	print(output)

def printTableRow(trans_, devanagari_, brahmi_):
	print(f"""	<tr>
		<td>{trans_}</td>
		<td>{devanagari_}</td>
		<td>{brahmi_}</td>
	</tr>""")

if __name__ == "__main__":
	#printArray(data1.split("\t"), "trans")
	#printArray(data2.split("\t"), "brahmi")
	#printArray(data3.split("\t"), "devanagari")
	trans = ["k-", "kh-", "g-", "gh-", "ṅ-", "c-", "ch-", "j-", "jh-", "ñ-", "ṭ-", "ṭh-", "ḍ-", "ḍh-", "ṇ-", "t-", "th-", "d-", "dh-", "n-", "p-", "ph-", "b-", "bh-", "m-", "y-", "r-", "l-", "v-", "ś-", "ṣ-", "s-", "h-"]
	brahmi = ["𑀓", "𑀔", "𑀕", "𑀖", "𑀗", "𑀘", "𑀙", "𑀚", "𑀛", "𑀜", "𑀝", "𑀞", "𑀟", "𑀠", "𑀡", "𑀢", "𑀣", "𑀤", "𑀥", "𑀦", "𑀧", "𑀨", "𑀩", "𑀪", "𑀫", "𑀬", "𑀭", "𑀮", "𑀯", "𑀰", "𑀱", "𑀲", "𑀳"]
	devanagari = ["क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह"]

	x = 0
	while x < len(trans):
		printTableRow(trans[x], devanagari[x], brahmi[x])
		x+=1

