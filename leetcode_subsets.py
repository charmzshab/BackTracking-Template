def is_valid_state(self,state, nums):
    # check if it is a valid solution
    return state <= nums

def get_candidates(self,state,nums):
    if not state:
        return nums
    candidates = []
    for num in nums:
        if num not in state:
            candidates.append(num)
    return candidates

def search(self,state, nums, solutions):
    if self.is_valid_state(state, nums):
        solutions.append(state.copy())
    for candidate in self.get_candidates(state, nums):
        state.add(candidate)
        self.search(state, nums, solutions)
        state.remove(candidate)

def subsets(self, nums: List[int]) -> List[List[int]]:
    solutions = []
    state = set()
    self.search(state, nums, solutions)
    return solutions
