//Problem Link: https://leetcode.com/problems/build-array-from-permutation/description/

//Solution
class build_array_from_permutation {
    public int[] buildArray(int[] nums) {
        for(int i=0; i < nums.length; i++) {
            int x = nums[i];
            int y = nums[x];
            int sum = nums[x] + nums[y];
            nums[x] = sum - nums[x];
            nums[i] = sum - nums[i];
        }
        return nums;
    }
}
