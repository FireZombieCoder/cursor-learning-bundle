// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SimpleStorage
 * @dev A contract to demonstrate storage, memory, and calldata concepts
 * @author Base Learning Curriculum
 */
contract SimpleStorage {
    // Storage variables (persistent on blockchain)
    uint256 public storedData;
    string public storedString;
    address public owner;
    bool public isLocked;
    
    // Struct to demonstrate complex data types
    struct UserData {
        string name;
        uint256 age;
        bool isActive;
    }
    
    // Storage mapping
    mapping(address => UserData) public users;
    
    // Events
    event DataStored(uint256 indexed newData, address indexed setter);
    event StringStored(string newString, address indexed setter);
    event UserRegistered(address indexed user, string name, uint256 age);
    event ContractLocked(address indexed locker);
    
    // Custom errors
    error Unauthorized();
    error ContractLocked();
    error InvalidAge();
    error EmptyName();
    
    modifier onlyOwner() {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }
    
    modifier notLocked() {
        if (isLocked) revert ContractLocked();
        _;
    }
    
    constructor() {
        owner = msg.sender;
        storedData = 0;
        storedString = "Initial String";
        isLocked = false;
    }
    
    /**
     * @dev Store a uint256 value
     * @param _data The value to store
     */
    function store(uint256 _data) external notLocked {
        storedData = _data;
        emit DataStored(_data, msg.sender);
    }
    
    /**
     * @dev Store a string value
     * @param _string The string to store
     */
    function storeString(string calldata _string) external notLocked {
        if (bytes(_string).length == 0) revert EmptyName();
        storedString = _string;
        emit StringStored(_string, msg.sender);
    }
    
    /**
     * @dev Register user data
     * @param _name User's name
     * @param _age User's age
     */
    function registerUser(string calldata _name, uint256 _age) external notLocked {
        if (bytes(_name).length == 0) revert EmptyName();
        if (_age == 0 || _age > 150) revert InvalidAge();
        
        users[msg.sender] = UserData({
            name: _name,
            age: _age,
            isActive: true
        });
        
        emit UserRegistered(msg.sender, _name, _age);
    }
    
    /**
     * @dev Get user data
     * @param _user The user's address
     * @return name The user's name
     * @return age The user's age
     * @return isActive Whether the user is active
     */
    function getUserData(address _user) external view returns (string memory name, uint256 age, bool isActive) {
        UserData memory user = users[_user];
        return (user.name, user.age, user.isActive);
    }
    
    /**
     * @dev Lock the contract (only owner)
     */
    function lockContract() external onlyOwner {
        isLocked = true;
        emit ContractLocked(msg.sender);
    }
    
    /**
     * @dev Get contract state
     * @return data The stored uint256 data
     * @return stringData The stored string data
     * @return contractOwner The contract owner
     * @return locked Whether the contract is locked
     */
    function getContractState() external view returns (
        uint256 data,
        string memory stringData,
        address contractOwner,
        bool locked
    ) {
        return (storedData, storedString, owner, isLocked);
    }
    
    /**
     * @dev Demonstrate memory vs storage
     * @param _input Input value
     * @return result The result of the calculation
     */
    function demonstrateMemory(uint256 _input) external pure returns (uint256 result) {
        // Memory variables (temporary, cheaper)
        uint256 memoryVar = _input * 2;
        uint256 anotherMemoryVar = memoryVar + 10;
        
        // Return the result (memory variables are discarded after function execution)
        return anotherMemoryVar;
    }
}
