// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title HelloBase
 * @dev A simple contract to demonstrate basic Solidity concepts and Base deployment
 * @author Base Learning Curriculum
 */
contract HelloBase {
    string public message;
    address public immutable owner;

    // Events for logging important state changes
    event MessageUpdated(string newMessage, address indexed updater);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Custom errors for gas-efficient error handling
    error Unauthorized();
    error EmptyMessage();
    error SameMessage();

    /**
     * @dev Constructor sets the initial message and owner
     * @param _message The initial message to store
     */
    constructor(string memory _message) {
        if (bytes(_message).length == 0) revert EmptyMessage();
        message = _message;
        owner = msg.sender;
    }

    /**
     * @dev Updates the stored message
     * @param _newMessage The new message to store
     * Requirements:
     * - Only the owner can update the message
     * - The new message cannot be empty
     * - The new message must be different from the current message
     */
    function updateMessage(string calldata _newMessage) external {
        if (msg.sender != owner) revert Unauthorized();
        if (bytes(_newMessage).length == 0) revert EmptyMessage();
        if (keccak256(bytes(_newMessage)) == keccak256(bytes(message))) revert SameMessage();

        message = _newMessage;
        emit MessageUpdated(_newMessage, msg.sender);
    }

    /**
     * @dev Returns the current message
     * @return The current stored message
     */
    function getMessage() external view returns (string memory) {
        return message;
    }

    /**
     * @dev Returns the contract owner
     * @return The address of the contract owner
     */
    function getOwner() external view returns (address) {
        return owner;
    }

    /**
     * @dev Returns the length of the current message
     * @return The length of the message in bytes
     */
    function getMessageLength() external view returns (uint256) {
        return bytes(message).length;
    }

    /**
     * @dev Checks if a given address is the owner
     * @param _address The address to check
     * @return True if the address is the owner, false otherwise
     */
    function isOwner(address _address) external view returns (bool) {
        return _address == owner;
    }
}
