nums1 = [1, 2]
nums2 = [3, 4]

ln1 = len(nums1)
ln2 = len(nums2)

med1 = 0
med2 = 0
if ln1 > 0:
    med1 = (nums1[ln1//2-1] + nums1[ln1//2]) / 2 if ln1 % 2 == 0 else nums1[ln1//2]
if ln2 > 0:
    med2 = (nums2[ln2//2-1] + nums2[ln2//2]) / 2 if ln2 % 2 == 0 else nums2[ln2//2]

if med1 == 0:
    print(med2)
elif med2 == 0:
    print(med1)
else:
    print(med1,med2)
    print((med1 + med2) / 2)


