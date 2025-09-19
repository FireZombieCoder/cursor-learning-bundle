// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol";
import "../contracts/stage0/HelloBase.sol";

/**
 * @title DeployHelloBase
 * @dev Deployment script for the HelloBase contract
 * @author Base Learning Curriculum
 */
contract DeployHelloBase is Script {
    function run() external {
        uint256 deployerPrivateKey = vm.envUint("PRIVATE_KEY");
        address deployer = vm.addr(deployerPrivateKey);

        console.log("Deploying contracts with account:", deployer);
        console.log("Account balance:", deployer.balance);

        vm.startBroadcast(deployerPrivateKey);

        HelloBase helloBase = new HelloBase("Hello Base Sepolia!");

        vm.stopBroadcast();

        console.log("HelloBase deployed to:", address(helloBase));
        console.log("Initial message:", helloBase.message());
        console.log("Contract owner:", helloBase.owner());
    }
}
