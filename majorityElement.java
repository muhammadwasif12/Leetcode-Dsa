public int majorityElement(int[] nums) {
    int n = nums.length;
    for (int i = 0; i < n; i++) {
        int count = 0;
        // Count occurrences of nums[i]
        for (int j = 0; j < n; j++) {
            if (nums[j] == nums[i]) {
                count++;
            }
        }
        // If count exceed n/2, nums[i] is the majority element
        if (count > n / 2) {
            return nums[i];
        }
    }
    return -1; // Should never be reached if majority element assumption holds
}