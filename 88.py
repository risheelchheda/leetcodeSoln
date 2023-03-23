if nums1==[0]:
            nums1[0]=nums2[0]
        left=m-1
        right=n-1
        end=n+m-1
        while right>=0 and left>=0:
            if nums1[left]>=nums2[right]:
                nums1[end]=nums1[left]
                end-=1
                left-=1
            elif nums1[left]<nums2[right]:
                nums1[end]=nums2[right]
                end-=1
                right-=1
        while right>=0:
            nums1[end]=nums2[right]
            right-=1
            end-=1
