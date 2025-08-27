class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int[] rotated = new int[n];
        k = k % n; // Handle cases where k >= n
        
        // Place elements in the new positions
        for (int i = 0; i < n; i++) {
            rotated[(i + k) % n] = nums[i];
        }
        
        // Copy the content of rotated array to the original array
        for (int i = 0; i < n; i++) {
            nums[i] = rotated[i];
        }
    }
}


