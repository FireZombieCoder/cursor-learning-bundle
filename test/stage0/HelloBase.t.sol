// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../../contracts/stage0/HelloBase.sol";

/**
 * @title HelloBaseTest
 * @dev Comprehensive tests for the HelloBase contract
 * @author Base Learning Curriculum
 */
contract HelloBaseTest is Test {
    HelloBase public helloBase;
    address public owner = address(1);
    address public user = address(2);
    address public anotherUser = address(3);

    event MessageUpdated(string newMessage, address indexed updater);

    function setUp() public {
        // Deploy contract with owner as msg.sender
        vm.prank(owner);
        helloBase = new HelloBase("Initial Message");
    }

    function testInitialState() public {
        assertEq(helloBase.message(), "Initial Message");
        assertEq(helloBase.owner(), owner);
        assertEq(helloBase.getMessageLength(), 15); // "Initial Message" length
        assertTrue(helloBase.isOwner(owner));
        assertFalse(helloBase.isOwner(user));
    }

    function testUpdateMessage() public {
        string memory newMessage = "Updated Message";

        vm.expectEmit(true, true, true, true);
        emit MessageUpdated(newMessage, owner);

        vm.prank(owner);
        helloBase.updateMessage(newMessage);

        assertEq(helloBase.message(), newMessage);
        assertEq(helloBase.getMessageLength(), 15); // "Updated Message" length
    }

    function testUnauthorizedUpdate() public {
        vm.prank(user);
        vm.expectRevert(HelloBase.Unauthorized.selector);
        helloBase.updateMessage("Hacked Message");

        // Message should remain unchanged
        assertEq(helloBase.message(), "Initial Message");
    }

    function testEmptyMessage() public {
        vm.prank(owner);
        vm.expectRevert(HelloBase.EmptyMessage.selector);
        helloBase.updateMessage("");
    }

    function testSameMessage() public {
        vm.prank(owner);
        vm.expectRevert(HelloBase.SameMessage.selector);
        helloBase.updateMessage("Initial Message");
    }

    function testMultipleUpdates() public {
        string[] memory messages = new string[](3);
        messages[0] = "First Update";
        messages[1] = "Second Update";
        messages[2] = "Third Update";

        for (uint256 i = 0; i < messages.length; i++) {
            vm.prank(owner);
            helloBase.updateMessage(messages[i]);
            assertEq(helloBase.message(), messages[i]);
        }
    }

    function testGetMessage() public {
        string memory retrievedMessage = helloBase.getMessage();
        assertEq(retrievedMessage, "Initial Message");
    }

    function testGetOwner() public {
        address retrievedOwner = helloBase.getOwner();
        assertEq(retrievedOwner, owner);
    }

    function testIsOwner() public {
        assertTrue(helloBase.isOwner(owner));
        assertFalse(helloBase.isOwner(user));
        assertFalse(helloBase.isOwner(address(0)));
    }

    function testGetMessageLength() public {
        assertEq(helloBase.getMessageLength(), 15); // "Initial Message"

        vm.prank(owner);
        helloBase.updateMessage("Short");
        assertEq(helloBase.getMessageLength(), 5);

        vm.prank(owner);
        helloBase.updateMessage("This is a much longer message to test length calculation");
        assertEq(helloBase.getMessageLength(), 58);
    }

    function testEventEmission() public {
        string memory testMessage = "Event Test Message";

        // Expect the event to be emitted
        vm.expectEmit(true, true, true, true);
        emit MessageUpdated(testMessage, owner);

        vm.prank(owner);
        helloBase.updateMessage(testMessage);
    }

    function testGasUsage() public {
        // Test gas usage for different operations
        uint256 gasBefore = gasleft();

        vm.prank(owner);
        helloBase.updateMessage("Gas Test Message");

        uint256 gasUsed = gasBefore - gasleft();

        // Gas usage should be reasonable (less than 100k gas)
        assertLt(gasUsed, 100000);

        // Log gas usage for analysis
        console.log("Gas used for updateMessage:", gasUsed);
    }

    function testFuzzUpdateMessage(string calldata _message) public {
        // Skip empty messages and same messages
        vm.assume(bytes(_message).length > 0);
        vm.assume(keccak256(bytes(_message)) != keccak256(bytes("Initial Message")));

        vm.prank(owner);
        helloBase.updateMessage(_message);

        assertEq(helloBase.message(), _message);
        assertEq(helloBase.getMessageLength(), bytes(_message).length);
    }

    function testFuzzIsOwner(address _address) public {
        bool expected = (_address == owner);
        assertEq(helloBase.isOwner(_address), expected);
    }
}
