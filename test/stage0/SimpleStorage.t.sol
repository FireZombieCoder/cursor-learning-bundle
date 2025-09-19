// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../../contracts/stage0/SimpleStorage.sol";

/**
 * @title SimpleStorageTest
 * @dev Comprehensive tests for the SimpleStorage contract
 * @author Base Learning Curriculum
 */
contract SimpleStorageTest is Test {
    SimpleStorage public simpleStorage;
    address public owner = address(1);
    address public user = address(2);
    address public anotherUser = address(3);

    event DataStored(uint256 indexed newData, address indexed setter);
    event StringStored(string newString, address indexed setter);
    event UserRegistered(address indexed user, string name, uint256 age);
    event ContractLocked(address indexed locker);

    function setUp() public {
        vm.prank(owner);
        simpleStorage = new SimpleStorage();
    }

    function testInitialState() public {
        assertEq(simpleStorage.storedData(), 0);
        assertEq(simpleStorage.storedString(), "Initial String");
        assertEq(simpleStorage.owner(), owner);
        assertFalse(simpleStorage.isLocked());
    }

    function testStoreData() public {
        uint256 testData = 42;

        vm.expectEmit(true, true, true, true);
        emit DataStored(testData, user);

        vm.prank(user);
        simpleStorage.store(testData);

        assertEq(simpleStorage.storedData(), testData);
    }

    function testStoreString() public {
        string memory testString = "Test String";

        vm.expectEmit(true, true, true, true);
        emit StringStored(testString, user);

        vm.prank(user);
        simpleStorage.storeString(testString);

        assertEq(simpleStorage.storedString(), testString);
    }

    function testEmptyString() public {
        vm.prank(user);
        vm.expectRevert(SimpleStorage.EmptyName.selector);
        simpleStorage.storeString("");
    }

    function testRegisterUser() public {
        string memory userName = "Alice";
        uint256 userAge = 25;

        vm.expectEmit(true, true, true, true);
        emit UserRegistered(user, userName, userAge);

        vm.prank(user);
        simpleStorage.registerUser(userName, userAge);

        (string memory name, uint256 age, bool isActive) = simpleStorage.getUserData(user);
        assertEq(name, userName);
        assertEq(age, userAge);
        assertTrue(isActive);
    }

    function testInvalidAge() public {
        vm.prank(user);
        vm.expectRevert(SimpleStorage.InvalidAge.selector);
        simpleStorage.registerUser("Alice", 0);

        vm.prank(user);
        vm.expectRevert(SimpleStorage.InvalidAge.selector);
        simpleStorage.registerUser("Alice", 151);
    }

    function testEmptyNameRegistration() public {
        vm.prank(user);
        vm.expectRevert(SimpleStorage.EmptyName.selector);
        simpleStorage.registerUser("", 25);
    }

    function testLockContract() public {
        vm.expectEmit(true, true, true, true);
        emit ContractLocked(owner);

        vm.prank(owner);
        simpleStorage.lockContract();

        assertTrue(simpleStorage.isLocked());
    }

    function testUnauthorizedLock() public {
        vm.prank(user);
        vm.expectRevert(SimpleStorage.Unauthorized.selector);
        simpleStorage.lockContract();
    }

    function testOperationsAfterLock() public {
        // Lock the contract
        vm.prank(owner);
        simpleStorage.lockContract();

        // Try to store data after lock
        vm.prank(user);
        vm.expectRevert(SimpleStorage.ContractLocked.selector);
        simpleStorage.store(42);

        // Try to store string after lock
        vm.prank(user);
        vm.expectRevert(SimpleStorage.ContractLocked.selector);
        simpleStorage.storeString("Test");

        // Try to register user after lock
        vm.prank(user);
        vm.expectRevert(SimpleStorage.ContractLocked.selector);
        simpleStorage.registerUser("Alice", 25);
    }

    function testGetContractState() public {
        vm.prank(user);
        simpleStorage.store(123);

        vm.prank(anotherUser);
        simpleStorage.storeString("Updated String");

        (
            uint256 data,
            string memory stringData,
            address contractOwner,
            bool locked
        ) = simpleStorage.getContractState();

        assertEq(data, 123);
        assertEq(stringData, "Updated String");
        assertEq(contractOwner, owner);
        assertFalse(locked);
    }

    function testDemonstrateMemory() public {
        uint256 input = 10;
        uint256 result = simpleStorage.demonstrateMemory(input);

        // Should return (input * 2) + 10 = (10 * 2) + 10 = 30
        assertEq(result, 30);
    }

    function testMultipleUsers() public {
        // Register multiple users
        vm.prank(user);
        simpleStorage.registerUser("Alice", 25);

        vm.prank(anotherUser);
        simpleStorage.registerUser("Bob", 30);

        // Check user data
        (string memory aliceName, uint256 aliceAge, bool aliceActive) = simpleStorage.getUserData(user);
        assertEq(aliceName, "Alice");
        assertEq(aliceAge, 25);
        assertTrue(aliceActive);

        (string memory bobName, uint256 bobAge, bool bobActive) = simpleStorage.getUserData(anotherUser);
        assertEq(bobName, "Bob");
        assertEq(bobAge, 30);
        assertTrue(bobActive);
    }

    function testFuzzStoreData(uint256 _data) public {
        vm.prank(user);
        simpleStorage.store(_data);

        assertEq(simpleStorage.storedData(), _data);
    }

    function testFuzzStoreString(string calldata _string) public {
        vm.assume(bytes(_string).length > 0);

        vm.prank(user);
        simpleStorage.storeString(_string);

        assertEq(simpleStorage.storedString(), _string);
    }

    function testFuzzRegisterUser(string calldata _name, uint256 _age) public {
        vm.assume(bytes(_name).length > 0);
        vm.assume(_age > 0 && _age <= 150);

        vm.prank(user);
        simpleStorage.registerUser(_name, _age);

        (string memory name, uint256 age, bool isActive) = simpleStorage.getUserData(user);
        assertEq(name, _name);
        assertEq(age, _age);
        assertTrue(isActive);
    }

    function testGasUsage() public {
        uint256 gasBefore = gasleft();

        vm.prank(user);
        simpleStorage.store(42);

        uint256 gasUsed = gasBefore - gasleft();

        // Gas usage should be reasonable
        assertLt(gasUsed, 100000);

        console.log("Gas used for store:", gasUsed);
    }
}
